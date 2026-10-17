from core.api.student_service.assertions.student_assertions import StudentAssertBase
from core.api.student_service.student_controller import StudentController
from tests.functional.student_service.settings import SERVICE_URL

import pytest
import logging

logger = logging.getLogger()
student_checker = StudentAssertBase()


class TestGetStudents:
    student_ctrl = StudentController()

    def test_get_students(self):
        logger.info('Starting tests for endpoint "GET /students/"')

        response = self.student_ctrl.get_students(base_url=SERVICE_URL, expected_status_code=200)
        students = response.json()
        assert len(students) > 0

    @pytest.mark.parametrize('sort_by',
                             ['id', '-id', 'name', '-name', 'score', '-score'])
    def test_get_students_check_sorting(self, sort_by):
        logger.info(f'Starting tests for endpoint "GET /students/" with sorting by "{sort_by}"')

        response = self.student_ctrl.get_students(base_url=SERVICE_URL, query_params={"sort_by": sort_by})
        students = response.json()
        student_checker.check_students_are_sorted_by_param(students, sort_by)
