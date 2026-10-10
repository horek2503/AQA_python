from core.api.student_service.assertions.student_assertions import StudentAssertBase
from core.api.student_service.student_controller import StudentController
import pytest
import logging

logger = logging.getLogger()
student_id = 1
student_checker = StudentAssertBase()


class TestGetStudents:
    student_ctrl = StudentController()
    service_url = 'http://127.0.0.1:8080'

    def test_get_students(self):
        logger.info('Starting tests for endpoint "GET /students/"')

        response = self.student_ctrl.get_students(base_url=self.service_url)
        students = response.json()

        assert response.status_code == 200
        assert len(students) > 0
        for student in students:
            student_checker.check_student_response_structure(student)


    @pytest.mark.parametrize('sort_by',
                             ['id', '-id', 'name', '-name', 'score', '-score'])
    def test_get_students_check_sorting(self, sort_by):
        # logger.info(f'Starting tests for endpoint "GET /students/" with sorting by "{sort_by}"')

        response = self.student_ctrl.get_students(base_url=self.service_url, query_params={"sort_by": sort_by})
        students = response.json()

        student_checker.check_students_are_sorted_by_param(students, sort_by)
