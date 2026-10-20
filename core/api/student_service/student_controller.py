import logging
import requests
from curlify import to_curl

from core.api.student_service.DTOs.student_schema import StudentSchema

logger = logging.getLogger()


class StudentController:

    def __init__(self):
        self.__token = None

    def get_students(self, base_url, query_params=None, expected_status_code=200):
        response = requests.get(url=f'{base_url}/students', params=query_params)
        self.log_curl(response.request)

        assert response.status_code == expected_status_code, f'Status code {response.status_code} doesn\'t match expected {expected_status_code}'
        StudentSchema(many=True).load(response.json())

        return response

    def get_student(self, base_url, student_id, query_params=None, expected_status_code=200):
        response = requests.get(url=f'{base_url}/students/{student_id}', params=query_params)
        self.log_curl(response.request)

        assert response.status_code == expected_status_code, f'Status code {response.status_code} doesn\'t match expected {expected_status_code}'
        StudentSchema().load(response.json())

        return response

    def post_student(self, base_url, request_body: dict, use_token: bool = True, expected_status_code=201,
                     validate_schema=True):
        if use_token:
            if self.__token is None:
                self.__get_token(base_url)
            headers = {'token': self.__token}
        else:
            headers = {}
        response = requests.post(url=f'{base_url}/students', json=request_body, headers=headers)
        self.log_curl(response.request)

        if validate_schema:
            StudentSchema().load(response.json())
        assert response.status_code == expected_status_code, f'Status code {response.status_code} doesn\'t match expected {expected_status_code}'

        return response

    def put_student(self, base_url, student_id: int, request_body: dict, use_token: bool = True,
                    expected_status_code=200,
                    validate_schema=True):
        if use_token:
            if self.__token is None:
                self.__get_token(base_url)
            headers = {'token': self.__token}
        else:
            headers = {}
        response = requests.put(url=f'{base_url}/students/{student_id}', json=request_body, headers=headers)
        self.log_curl(response.request)

        if validate_schema:
            StudentSchema().load(response.json())
        assert response.status_code == expected_status_code, f'Status code {response.status_code} doesn\'t match expected {expected_status_code}'

        return response

    def delete_student(self, base_url, student_id: int, expected_status_code=204):
        if self.__token is None:
            self.__get_token(base_url)
        headers = {'token': self.__token}

        response = requests.delete(url=f'{base_url}/students/{student_id}', headers=headers)
        self.log_curl(response.request)

        assert response.status_code == expected_status_code, \
            f'Status code {response.status_code} doesn\'t match expected {expected_status_code}'

        return response

    def log_curl(self, request):
        curl = to_curl(request)
        logger.info(f'CURL: "{curl}"')

    def __get_token(self, base_url, username='test', password='test'):
        response = requests.post(url=f'{base_url}/auth', json={"name": username, "password": password})
        self.log_curl(response.request)
        self.__token = response.text
