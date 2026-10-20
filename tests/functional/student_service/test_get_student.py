import pytest
import random
from assertpy import soft_assertions, assert_that
from tests.functional.student_service.conftest import TestStudentBase


class TestGetStudent(TestStudentBase):

    def get_random_existing_student_id(self):
        response = self.student_ctrl.get_students(base_url=self.SERVICE_URL, query_params={"limit": 1000})
        students = response.json()
        all_ids = [student['id'] for student in students]

        return random.choice(all_ids)

    @pytest.mark.parametrize('student_id, expected_name, expected_score',
                             [
                                 (1, 'Jennifer Estrada', 48),
                                 (3, 'Michelle Myers', 64),
                                 (5, 'Edwin Thompson', 50),
                                 (7, 'Jessica Walter', 11),
                                 (9, 'George White', 1)
                             ])
    def test_get_student_by_id_from_fixed_set(self, student_id, expected_name, expected_score):

        self.logger.info(f'Starting tests for endpoint "GET /students/{student_id}"...')
        response = self.student_ctrl.get_student(base_url=self.SERVICE_URL, student_id=student_id, expected_status_code=200)
        student = response.json()
        with soft_assertions():
            assert_that(student['id'], f'Student id mismatch: ER = {student_id}; AR = {student['id']}').is_equal_to(student_id)
            assert_that(student['name'], f'Student name mismatch: ER = {expected_name}; AR = {student['name']}').is_equal_to(expected_name)
            assert_that(student['score'], f'Student score mismatch: ER = {expected_score}; AR = {student['score']}').is_equal_to(expected_score)

    def test_check_student_score_name(self, student_id = None):
        student_id = student_id or self.get_random_existing_student_id()
        response = self.student_ctrl.get_student(base_url=self.SERVICE_URL, student_id=student_id,
                                                 expected_status_code=200)
        student = response.json()
        actual_score = student['score']
        actual_score_name = student['score_name']
        self.logger.info(f'Starting test "test_check_score_name_for_random_student" for student with id={student['id']}, score = {student['score']}, score_name ={
            student['score_name']}')
        if actual_score > 90:
            assert actual_score_name == 'GREAT', f'Score name "BAD" expected for score > 90, but got {actual_score_name}'
        elif actual_score > 50:
            assert actual_score_name == 'GOOD', f'Score name "GOOD" expected for score between 50 and 90, but got {actual_score_name}'
        else:
            assert actual_score_name == 'BAD', f'Score name "BAD" expected for score < 50, but got {actual_score_name}'
