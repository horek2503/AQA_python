from core.api.student_service.assertions.student_assertions import StudentAssertBase
from core.api.student_service.student_controller import StudentController
import pytest
import logging

logger = logging.getLogger()
student_id = 1
student_checker = StudentAssertBase()


class TestGetStudent:
    student_ctrl = StudentController()
    service_url = 'http://127.0.0.1:8080'

    def test_get_student_by_id(self):
        logger.info(f'Starting tests for endpoint "GET /students/{student_id}"')
        response = self.student_ctrl.get_student(base_url=self.service_url, student_id=student_id, expected_status_code=200)
        # assert response.status_code == 200 # -> instead we check in controller via "expected_status_code"
        student = response.json()
        # student_checker.check_student_response_structure(student) # -> instead we check in controller via marshmallow
        assert student['id'] == 1
