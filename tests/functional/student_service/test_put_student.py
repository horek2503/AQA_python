import random
from faker import Faker
from tests.functional.student_service.conftest import TestStudentBase

faker = Faker()

class TestPutStudent(TestStudentBase):

    def test_put_student_score(self, create_and_delete_student):
        student = create_and_delete_student
        self.logger.info(f'Starting test "test_put_student_score" for student with id = {student['id']}, score =  {student['score']}')
        target_score = random.randint(1,100)
        upd_user_data = {
            'score': target_score
        }
        upd_student_response = self.student_ctrl.put_student(
            base_url=self.SERVICE_URL,
            student_id=student['id'],
            request_body=upd_user_data, expected_status_code=200)

        upd_student = upd_student_response.json()

        assert upd_student['score'] == target_score, f'Updated student score must be {target_score}'

    def test_put_student_name(self, create_and_delete_student):
        student = create_and_delete_student
        self.logger.info(f'Starting test "test_put_student_name" for student with id = {student['id']}, name = {student['name']}')
        target_name = faker.name()
        upd_user_data = {
            'name': target_name
        }
        upd_student_response = self.student_ctrl.put_student(
            base_url=self.SERVICE_URL,
            student_id=student['id'],
            request_body=upd_user_data, expected_status_code=200)

        upd_student = upd_student_response.json()

        assert upd_student['name'] == target_name, f"Updated student name must be {target_name}"
