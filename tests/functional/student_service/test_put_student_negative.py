import pytest
from tests.functional.student_service.conftest import TestStudentBase


class TestPutStudentNegative(TestStudentBase):

    @pytest.mark.parametrize('score',
                             [-1, 101, 'string', {}, [], None])
    def test_put_student_invalid_score_negative(self, create_and_delete_student, score):
        self.logger.info(f'Starting test "test_put_student_invalid_score_negative" with score = {score}')
        student = create_and_delete_student

        upd_user_data = {
            'score': score
        }
        self.student_ctrl.put_student(
            base_url=self.SERVICE_URL,
            student_id=student['id'],
            request_body=upd_user_data,
            expected_status_code=400,
            validate_schema=False
        )

    @pytest.mark.parametrize('name',
                             [999, {}, '', None])
    def test_put_student_invalid_name_negative(self, create_and_delete_student, name):
        self.logger.info(f'Starting test "test_put_student_invalid_name_negative" with name={name}')
        student = create_and_delete_student

        upd_user_data = {
            'name': name
        }
        self.student_ctrl.put_student(
            base_url=self.SERVICE_URL,
            student_id=student['id'],
            request_body=upd_user_data,
            expected_status_code=400,
            validate_schema=False
        )