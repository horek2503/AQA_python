import random
from faker import Faker
import secrets.db_secrets as s
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, select
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
    try:
        session.add(student)
        session.commit()
        return student.id
    except Exception as e:
        print(f'Cannot create user {firstName}. Exception is {e}')
        session.rollback()


def assign_student_to_courses(student_id: int, course_names: list):
    if course_names:
        for course_name in course_names:
            try:
                student = session.query(Student).filter_by(id=student_id).first()
                course = session.query(Course).filter_by(name=course_name).first()
                student.courses.append(course)
                session.commit()
            except Exception as e:
                print(f"Cannot assign student to course. Exception is {e}")
                session.rollback()


def delete_student_by_id(student_id: int):
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        session.delete(student)
        session.commit()
        print(f'Student with id={student_id} is deleted.')
    except Exception as e:
        print(f"Cannot delete student. Exception is {e}")
        session.rollback()


def get_courses_by_student_id(student_id: int):
    try:
        student = session.query(Student).filter_by(id=student_id).first()
        course_names = [x.name for x in student.courses]
        return course_names
    except Exception as e:
        print(f"Cannot get student courses. Exception is {e}")


def get_students_by_course_id(course_id: int):
    try:
        students = session.query(studentToCourse).filter_by(course_id=course_id).all()
        student_ids = [x[0] for x in students]
        select_query = select(Student).where(Student.id.in_((student_ids)))
        results = session.execute(select_query)
        names = [k[0] for k in results.fetchall()]
        full_names = [f'{x.firstName} {x.secondName}' for x in names]
        return full_names
    except Exception as e:
        print(f"Cannot get students by course. Exception is {e}")


def create_courses_if_not_exist():
    available_courses = ['Math', 'Art', 'Computer science', 'History', 'Biology']
    existing_courses = session.query(Course).all()
    if len(existing_courses) < 5:
        for course_name in available_courses:
            course = Course(name=course_name)
            try:
                session.add(course)
                session.commit()
            except Exception as e:
                print(f"Cannot create course '{course_name}'. Exception is {e}")
                session.rollback()


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

# Generating random students and fixed 5 courses
create_courses_if_not_exist()
generate_students_till_n()
randomly_distribute_students_among_courses()

# CRUD for student with certain parameters
print(f"\nCreating student 'Oleh Stoyanov'...")
student_id = create_student(firstName='Oleh', secondName='Stoyanov', passport='CV081972821a')
assign_student_to_courses(student_id, ['Math', 'History', 'Biology'])
print(f"Created student has id = {student_id} and attends the following courses:")
print(get_courses_by_student_id(student_id))
print(f'Deleting student with id = {student_id}...')
delete_student_by_id(student_id)

# Getting students attending particular course
print("\nStudents attending course with id = 1:")
print(get_students_by_course_id(1))
