import requests


class StudentController:

    def get_students(self, base_url, query_params=None):
        print(f'{base_url}/students')
        response = requests.get(url=f'{base_url}/students', params=query_params)
        return response

    def get_student(self):
        pass
