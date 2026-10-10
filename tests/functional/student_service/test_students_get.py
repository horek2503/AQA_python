from core.api.student_service.student_controller import StudentController


class TestGetStudents:

    student_ctrl = StudentController()
    service_url = 'http://127.0.0.1/8080'

    def test_get_students(self):

        students = self.student_ctrl.get_students(base_url=self.service_url)