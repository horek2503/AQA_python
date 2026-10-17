from core.api.student_service.student_controller import StudentController
import logging

logger = logging.getLogger()
student_ctrl = StudentController()
service_url = 'http://127.0.0.1:8080'

class TestPutStudent:

    def test_put_student_score(self, create_and_delete_student):
        logger.info(f'Starting test "test_put_student_score"')
        student = create_and_delete_student

        upd_user_data = {
            'score': 10
        }
        upd_student_response = student_ctrl.put_student(
            base_url=service_url,
            student_id=student['id'],
            request_body=upd_user_data, expected_status_code=200)

        upd_student = upd_student_response.json()

        assert upd_student['score'] == 10, 'Updated student score must be 10'

    def test_put_student_name(self, create_and_delete_student):
        logger.info(f'Starting test "test_put_student_name"')
        student = create_and_delete_student

        upd_user_data = {
            'name': 'Spy'
        }
        upd_student_response = student_ctrl.put_student(
            base_url=service_url,
            student_id=student['id'],
            request_body=upd_user_data, expected_status_code=200)

        upd_student = upd_student_response.json()

        assert upd_student['name'] == 'Spy', "Updated student name must be 'Spy'"
