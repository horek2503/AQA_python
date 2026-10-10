from core.api.student_service.assertions.student_assertions import StudentAssertBase
from core.api.student_service.student_controller import StudentController
import logging
import random
from faker import Faker

faker = Faker()
logger = logging.getLogger()
student_checker = StudentAssertBase()


class TestPostStudent:
    student_ctrl = StudentController()
    service_url = 'http://127.0.0.1:8080'

    def test_post_student(self):
        logger.info(f'Starting tests for endpoint "POST /students"')
        user_name = faker.name()
        user_score = random.randint(1,100)
        user_data = {
            'name': user_name,
            'score': user_score
        }
        response = self.student_ctrl.post_student(base_url=self.service_url, request_body = user_data)

        assert response.status_code == 201
        student = response.json()
        student_checker.check_student_response_structure(student)
        assert student['name'] == user_name
        assert student['score'] == user_score
