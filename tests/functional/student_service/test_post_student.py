import pytest
import random
from faker import Faker
from tests.functional.student_service.conftest import TestStudentBase

faker = Faker()

class TestPostStudent(TestStudentBase):
    student_to_delete_id = None

    def test_post_student(self, delete_student):
        self.logger.info(f'Starting tests for endpoint "POST /students"')
        user_name = faker.name()
        user_score = random.randint(1, 100)
        user_data = {
            'name': user_name,
            'score': user_score
        }
        response = self.student_ctrl.post_student(base_url=self.SERVICE_URL, request_body=user_data,
                                                  expected_status_code=201)
        student = response.json()
        __class__.student_to_delete_id = student['id']
        assert student['name'] == user_name
        assert student['score'] == user_score

    @pytest.fixture
    def delete_student(self):
        yield
        if __class__.student_to_delete_id:
            self.logger.info(f'Deleting created student "DELETE /students/id"')
            self.student_ctrl.delete_student(base_url=self.SERVICE_URL, student_id=__class__.student_to_delete_id,
                                             expected_status_code=204)
