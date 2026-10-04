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


def create_courses_if_not_exist(current_session):
    available_courses = ['Math', 'Art', 'Computer science', 'History', 'Biology']
    existing_courses = current_session.query(Course).all()
    if len(existing_courses) < 5:
        for course_name in available_courses:
            course = Course(name=course_name)
            try:
                current_session.add(course)
            except Exception as e:
                print(f"Cannot create course '{course_name}'. Exception is {e}")
            else:
                current_session.commit()


def generate_students_till_n(current_session, n: int = 20):
    desired_num_of_students = n
    existing_students = current_session.query(Student).all()
    num_of_students_to_create = desired_num_of_students - len(existing_students)
    # print(existing_students)
    if num_of_students_to_create:
        for _ in range(num_of_students_to_create):
            student = Student(firstName=faker.first_name(),
                              secondName=faker.last_name(),
                              phone=faker.basic_phone_number(),
                              passport=faker.passport_number())
            current_session.add(student)
            current_session.commit()


def randomly_distribute_students_among_courses():
    pass


DB_URL = f'postgresql://{s.DB_USER}:{s.DB_PASSWORD}@{s.DB_HOST}:{s.DB_PORT}/{s.DB_NAME}'
engine = create_engine(DB_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

create_courses_if_not_exist(session)
generate_students_till_n(session)

### try to link students and courses
# desired_student = session.query(Student).first()
desired_course = session.query(Course).filter_by(name='Math').first()
# desired_student.courses.append(desired_course)
desired_course.id = 90

### delete student + links to courses
# student_to_delete = session.query(Student).filter_by(id=83).first()
# session.delete(student_to_delete)

session.commit()
