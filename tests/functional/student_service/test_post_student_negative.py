from core.api.student_service.student_controller import StudentController
import logging

logger = logging.getLogger()

class TestPostStudent:
    student_ctrl = StudentController()
    service_url = 'http://127.0.0.1:8080'

    def test_post_student_without_auth_negative(self):
        logger.info(f'Starting negative test for endpoint "POST /students"')
        user_data = {
            'name': 'Test',
            'score': 100
        }
        response = self.student_ctrl.post_student(base_url=self.service_url, request_body = user_data, use_token=False)
        
        assert response.status_code == 401

