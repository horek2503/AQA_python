import logging
import requests
from curlify import to_curl

logger = logging.getLogger()


class StudentController:

    def __init__(self):
        self.__token = None

    def get_students(self, base_url, query_params=None):
        response = requests.get(url=f'{base_url}/students', params=query_params)
        self.log_curl(response.request)
        return response

    def get_student(self, base_url, student_id, query_params=None):
        response = requests.get(url=f'{base_url}/students/{student_id}', params=query_params)
        self.log_curl(response.request)
        return response

    def post_student(self, base_url, request_body: dict, use_token: bool = True):
        if use_token:
            if self.__token is None:
                self.__get_token(base_url)
            headers = {'token': self.__token}
        else:
            headers = {}
        response = requests.post(url=f'{base_url}/students', json=request_body, headers=headers)
        self.log_curl(response.request)
        return response

    def log_curl(self, request):
        curl = to_curl(request)
        logger.info(f'CURL: "{curl}"')

    def __get_token(self, base_url, username='test', password='test'):
        response = requests.post(url=f'{base_url}/auth', json={"name": username, "password": password})
        self.__token = response.text


# body = {
#     "name": "Ihor",
#     "score": 99
# }
#
# st = StudentController()
# print(st.post_student(base_url='http://127.0.0.1:8080', request_body=body))
