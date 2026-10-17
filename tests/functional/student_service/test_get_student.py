import logging
import pytest
from core.api.student_service.student_controller import StudentController
from tests.functional.student_service.settings import SERVICE_URL

logger = logging.getLogger()


class TestGetStudent:
    student_ctrl = StudentController()

    @pytest.mark.parametrize('student_id, expected_name, expected_score',
                             [
                                 (1, 'Jennifer Estrada', 48),
                                 (3, 'Michelle Myers', 64),
                                 (5, 'Edwin Thompson', 50),
                                 (7, 'Jessica Walter', 11),
                                 (9, 'George White', 1)
                             ])
    def test_get_student_by_id(self, student_id, expected_name, expected_score):

        logger.info(f'Starting tests for endpoint "GET /students/{student_id}"')
        response = self.student_ctrl.get_student(base_url=SERVICE_URL, student_id=student_id, expected_status_code=200)
        student = response.json()
        assert student['id'] == student_id
        assert student['name'] == expected_name
        assert student['score'] == expected_score
