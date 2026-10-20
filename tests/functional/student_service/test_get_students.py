import pytest
from core.api.student_service.assertions.student_assertions import StudentAssertBase
from tests.functional.student_service.conftest import TestStudentBase

student_checker = StudentAssertBase()


class TestGetStudents(TestStudentBase):

    def test_get_students(self):
        self.logger.info('Starting tests for endpoint "GET /students/"')

        response = self.student_ctrl.get_students(base_url=self.SERVICE_URL, expected_status_code=200)
        students = response.json()
        assert len(students) > 0

    @pytest.mark.parametrize('sort_by',
                             ['id', '-id', 'name', '-name', 'score', '-score'])
    def test_get_students_check_sorting(self, sort_by):
        self.logger.info(f'Starting tests for endpoint "GET /students/" with sorting by "{sort_by}"')

        response = self.student_ctrl.get_students(base_url=self.SERVICE_URL, query_params={"sort_by": sort_by})
        students = response.json()
        student_checker.check_students_are_sorted_by_param(students, sort_by)

    @pytest.mark.parametrize('limit',
                             [None, 10, 15, 20, 100])
    def test_get_students_check_limit(self, limit):
        expected_limit = limit if limit else 10
        query_params = {"limit": limit} if limit else {}
        self.logger.info(f'Starting tests for endpoint "GET /students/" with limit = "{expected_limit}"')
        response = self.student_ctrl.get_students(base_url=self.SERVICE_URL, query_params=query_params)
        students = response.json()
        assert len(students) == expected_limit, f'"GET /students/" limit test failed. ER = {expected_limit}; AR = {len(students)}'
