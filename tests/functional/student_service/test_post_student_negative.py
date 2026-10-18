import pytest
from tests.functional.student_service.conftest import TestStudentBase


class TestPostStudentNegative(TestStudentBase):

    def test_post_student_without_auth_negative(self):
        self.logger.info(f'Starting negative test for endpoint "POST /students"')
        user_data = {
            'name': 'Test',
            'score': 100
        }
        self.student_ctrl.post_student(
            base_url=self.SERVICE_URL, request_body=user_data, use_token=False, expected_status_code=401,
            validate_schema=False)

    @pytest.mark.parametrize('score, expected_status_code',
                             [(-100, 400),
                              (101, 400),
                              ('str', 500)])
    def test_post_student_with_invalid_score_negative(self, score, expected_status_code):
        self.logger.info(f'Starting negative test for endpoint "POST /students"')
        user_data = {
            'name': 'Test',
            'score': score
        }
        self.student_ctrl.post_student(
            base_url=self.SERVICE_URL, request_body=user_data, use_token=True, expected_status_code=expected_status_code,
            validate_schema=False)