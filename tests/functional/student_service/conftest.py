
import pytest
from core.api.student_service.student_controller import StudentController
import logging
import random
from faker import Faker

faker = Faker()
logger = logging.getLogger()
student_ctrl = StudentController()
service_url = 'http://127.0.0.1:8080'


### FIXTURE SCOPE
# function - default
# class - виконується 1 раз для всіх тестів в class
# module - виконується 1 раз для всіх тестів в file
# package - виконується 1 раз для всіх тестів в package
# session - виконується 1 раз для всіх тестів

@pytest.fixture(scope="package")
def create_and_delete_student():
    user_name = faker.name()
    user_score = random.randint(1, 100)
    user_data = {
        'name': user_name,
        'score': user_score
    }
    response = student_ctrl.post_student(base_url=service_url, request_body=user_data,
                                         expected_status_code=201)
    student = response.json()

    yield student

    logger.info(f'Deleting created user "DELETE /students/id"')
    student_ctrl.delete_student(base_url=service_url, student_id=student['id'],
                                expected_status_code=204)

