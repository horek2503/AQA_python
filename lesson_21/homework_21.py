import random
from faker import Faker
import secrets.db_secrets as s
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, relationship

Base = declarative_base()
faker = Faker(locale='en_US')

studentToCourse = Table(
    'student_to_course',
    Base.metadata,
    Column('student_id',
           ForeignKey('students.id', name='student_to_course_student_id', ondelete='CASCADE', onupdate='CASCADE'),
           primary_key=True),
    Column('course_id',
           ForeignKey('courses.id', name='student_to_course_course_id', ondelete='CASCADE', onupdate='CASCADE'),
           primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String, nullable=False)
    secondName = Column(String, nullable=False)
    passport = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True)
    courses: Mapped[list['Course']] = relationship(
        secondary=studentToCourse,
        back_populates='students'
    )


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)
    students: Mapped[list['Student']] = relationship(
        secondary=studentToCourse,
        back_populates='courses'
    )


def create_student(firstName: str, secondName: str, passport: str, phone: str = None):
    student = Student(firstName=firstName,
                      secondName=secondName,
                      phone=phone,
                      passport=passport)
    session.add(student)

    try:
        session.commit()

    except Exception as e:
        print(f'Cannot create user {firstName}. Exception is {e}')
        session.rollback()


def assign_student_to_courses(student: Student, course_names: list):

    if course_names:
        for course_name in course_names:
            course = session.query(Course).filter_by(name=course_name).first()
            student.courses.append(course)
            try:
                session.commit()
            except Exception as e:
                print(f"Cannot assign student '{student.firstName}' to course {course_name}. Exception is {e}")
                session.rollback()


def create_courses_if_not_exist():
    available_courses = ['Math', 'Art', 'Computer science', 'History', 'Biology']
    existing_courses = session.query(Course).all()
    if len(existing_courses) < 5:
        for course_name in available_courses:
            course = Course(name=course_name)
            try:
                # session.begin()
                session.add(course)
            except Exception as e:
                print(f"Cannot create course '{course_name}'. Exception is {e}")
                session.rollback()
            else:
                session.commit()


def generate_students_till_n(desired_num_of_students: int = 20):
    existing_students = session.query(Student).all()
    num_of_students_to_create = desired_num_of_students - len(existing_students)
    if num_of_students_to_create > 0:
        for _ in range(num_of_students_to_create):
            create_student(firstName=faker.first_name(), secondName=faker.last_name(), phone=faker.basic_phone_number(),
                           passport=faker.passport_number())


def randomly_distribute_students_among_courses():
    # Randomly assign every student to random courses if no course(s) assigned for him yet
    students = session.query(Student).all()
    courses = session.query(Course).all()
    if students and courses:
        for student in students:
            existing_student_course_relations = session.query(studentToCourse).filter_by(student_id=student.id).all()
            if not existing_student_course_relations:
                random_num_of_courses = random.randint(1, len(courses))
                random_courses = random.sample(courses, random_num_of_courses)
                student.courses.extend(random_courses)
                session.commit()


DB_URL = f'postgresql://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}'
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

create_courses_if_not_exist()
generate_students_till_n()
randomly_distribute_students_among_courses()



create_student(firstName='Oleh', secondName='Stoyanov', passport='CV081972821a')

### try to link students and courses
desired_student = session.query(Student).first()
desired_course = session.query(Course).filter_by(name='Math').first()
assign_student_to_courses(desired_student, ['Math'])

# desired_course.id = 90

### delete student + links to courses
# student_to_delete = session.query(Student).first()
# print(student_to_delete.id)
# session.delete(student_to_delete)
create_student(firstName='Oleh', secondName='Stoyanov', passport='CV081972821a')


session.close()
