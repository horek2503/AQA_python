import pytest
import logging
import random
from core.api.student_service.student_controller import StudentController
# from tests.functional.student_service.settings import SERVICE_URL
from faker import Faker

faker = Faker()

### FIXTURE SCOPE
# function - default
# class - виконується 1 раз для всіх тестів в class
# module - виконується 1 раз для всіх тестів в file
# package - виконується 1 раз для всіх тестів в package
# session - виконується 1 раз для всіх тестів

class TestStudentBase:
    student_ctrl = StudentController()
    logger = logging.getLogger()
    SERVICE_URL = 'http://127.0.0.1:8080'

    @pytest.fixture(scope="module")
    def create_and_delete_student(self):
        user_name = faker.name()
        user_score = random.randint(1, 100)
        user_data = {
            'name': user_name,
            'score': user_score
        }
        response = self.student_ctrl.post_student(base_url=self.SERVICE_URL, request_body=user_data, expected_status_code=201)
        student = response.json()

        yield student

        self.logger.info(f'Deleting created user "DELETE /students/id"')
        self.student_ctrl.delete_student(base_url=self.SERVICE_URL, student_id=student['id'], expected_status_code=204)
