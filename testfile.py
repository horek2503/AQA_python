"""
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance == 0:
            raise ValueError("Cannot withdraw all money!")
        self.__balance = balance

my_account = BankAccount(198234, 1000)
#
# try:
#     print(my_account.get_balance())
# except AttributeError as e:
#     print(f"Не можна отримати баланс напряму!\n\t {e}")
# else:
#     try:
#         my_account.set_balance(0)
#     except ValueError as e:
#         print(f"Помилка оновлення рахунку!\n\t {e}")
# finally:
#     print("Closing connection to the Bank...")

try:
    print('str' + 10)
except NameError as e:
    print(f"Variable not found: \n\t{e}")
except:
    print(f"No luck...")
else:
    print("All good")

"""
import random

# with open("input_file.txt", 'r') as file:
#     content = file.read()
#     print(content)

# file = None
# try:
#     file = open("input_file.txt", 'r')
#     print(f"Data is: {file.read()}")
# except Exception:
#     print ("Something went wrong...")
# finally:
#     if file:
#         file.close()
#         print("File is closed")
#
# with open("input_file.txt", 'w') as file:
#     file.write('New data')
#
# print (file)

"""
Умова:
Створіть файл з ім'ям "data.txt", в якому розмістіть цілі числа (кожне число на новому рядку).
Функція повинна мати ім’я “calculate_sum_from_file(filename)”
Напишіть програму, яка відкриває файл "data.txt" для читання та читає числа з файлу.
Підрахуйте суму всіх чисел, прочитаних з файлу.
Забезпечте обробку можливих виключень:
Обробіть виняток, якщо файл не знайдено. (FileNotFoundError). Функція повинна вертати строку “File not found”
Обробіть виняток, якщо зміст файлу містить нечислові значення. (ValueError). Функція повинна вертати строку “Invalid data in the file”
Виведіть суму чисел, якщо операція пройшла успішно. В іншому випадку виведіть інформацію про виняток, який виник.

Закрийте файл навіть у випадку виняткової ситуації.
"""
#
# def calculate_sum_from_file(filename):
#     file = None
#     try:
#         file = open(filename, 'r')
#         lines = file.readlines()
#         numbers = [int(x.strip()) for x in lines]
#     except FileNotFoundError:
#         result = "File not found"
#     except ValueError:
#         result = "Invalid data in the file"
#     else:
#         result = sum(numbers)
#     finally:
#         if file is not None:
#             file.close()
#     return result
#
# print(calculate_sum_from_file("data.txt"))


### TEST (lesson 14) preparation ###
# -----------------------------------------
import pytest
from assertpy import assert_that

"""
def capitalize_text(input_text: str):
    words = input_text.split()
    capitalized_words = [word.capitalize() for word in words]
    result_text = ' '.join(capitalized_words)
    return result_text

@pytest.mark.parametrize('input_string, expected_string',
                         [
                             ('let me say hallo to you','Let Me Say Hallo To You'),
                             ('12 levels OF MOST int THXS','12 Levels Of Most Int Thxs')
                         ])
def test_capitalize_text(input_string, expected_string):
    actual_string = capitalize_text(input_string)
    assert (actual_string == expected_string), f"No luck for '{input_string}'!!!"
"""

# -----------------------------------------
#
# def word_count(input_string: str) -> int:
#     words = input_string.split()
#     return len(words)
#
#
# @pytest.mark.parametrize('string, expected_result',
#                          [('let me be your friend', 5),
#                           ('12 let kre', 3),
#                           ('so how old are you my dear lady', 8)])
# def test_word_count(string, expected_result):
#     actual_length = word_count(string)
#     assert_that(actual_length).is_equal_to(expected_result)
#
# -----------------------------------------
#
# def concatenate_strings(list_of_strings: list[str], join_symbol: str):
#     return join_symbol.join(list_of_strings)
#
# # print(concatenate_strings(['some', 'items', 'are', 'in', 'the', 'list'], '+'))
#
# @pytest.mark.parametrize('list_of_strings, join_symbol, expected_result',
#                          [(['','','',''], '*', '***'),
#                           (['a','b','c','d','e'], '/', 'a/b/c/d/e'),
#                           (['go', 'where', 'you', 'came','from!'], ' ', 'go where you came from!')])
# def test_concatenate_strings(list_of_strings, join_symbol, expected_result):
#     actual_result = concatenate_strings(list_of_strings, join_symbol)
#     assert_that(actual_result,
#                 f'Function result for "{list_of_strings}" and "{join_symbol}" does NOT match ER!'
#                 ).is_equal_to(expected_result)

# -----------------------------------------
#
# def is_palindrome(input_string:str) -> bool:
#     return True if input_string == input_string[::-1] else False
#
# @pytest.mark.parametrize('source, er',
#                          [('soros', True),
#                           ('paragon', False),
#                           ('', True)])
# def test_is_palindrome(source, er):
#     assert_that(is_palindrome(source),
#                 f'Palindrome function failed for input: "{source}"'
#                 ).is_equal_to(er)

# -----------------------------------------
#
# test_data = {
#     'person1': {'gender': 'Male', 'height': 175},
#     'person2': {'gender': 'Female', 'height': 160},
#     'person3': {'gender': 'Male', 'height': 180},
#     'person4': {'gender': 'Male', 'height': 157},
#     'person5': {'gender': 'Male', 'height': 198},
#     'person6': {'gender': 'Female', 'height': 162},
#     'person7': {'gender': 'Male', 'height': 180},
#     'person8': {'gender': 'Female', 'height': 155},
#     'person9': {'gender': 'Male', 'height': 178},
#     'person10': {'gender': 'Male', 'height': 200}
# }
#
#
# def get_male_average_height(input_data: dict) -> int|float:
#     sum_of_male_height = 0
#     male_counter = 0
#
#     for key, value in input_data.items():
#         if value['gender'] == 'Male':
#             sum_of_male_height += value['height']
#             male_counter += 1
#
#     try:
#         result = round((sum_of_male_height / male_counter),2)
#     except ZeroDivisionError:
#         return -1
#     else:
#         return result
#
# print(get_male_average_height(test_data))

# -----------------------------------------
#
# employee_data = [
# 	{"name": "Azimova", "salary": 20000, "gender": "f"},
# 	{"name": "Borenko", "salary": 9000, "gender": "m"},
# 	{"name": "Vasilenko", "salary": 10000, "gender": "m"},
# 	{"name": "Zabolotna", "salary": 25000, "gender": "f"},
# 	{"name": "Koval", "salary": 35000, "gender": "m"},
# ]
#
# def return_employee_stats(input_data:dict):
#     max_salary = max([x['salary'] for x in input_data])
#     person_with_max_salary = sorted([x['name'] for x in input_data if x['salary'] == max_salary])[0]
#     minimal_male_salary = min([x['salary'] for x in input_data if x['gender'] == 'm'])
#     max_female_salary = max([x['salary'] for x in input_data if x['gender'] == 'f'])
#     result_tuple = tuple([person_with_max_salary, minimal_male_salary, max_female_salary])
#     return result_tuple#
# print(return_employee_stats(employee_data))

# -----------------------------------------

# from temp.my_package.my_functions import convert_tuple_to_list
# import sys
# from definitions import BASE_FOLDER
# sys.path.append(str(BASE_FOLDER))
# print(sys.path)
# from temp.my_package import convert_tuple_to_list
#
# print(convert_tuple_to_list((1,2,3)))

# -----------------------------------------
# import random
#
# class MyIterable:
#     def __init__(self, n:int):
#         self.__n = n
#         self.__current = 0
#         self.__value = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.__current < self.__n:
#             self.__current += 1
#             self.get_value()
#             return self.__value
#         else:
#             raise StopIteration
#
#     def get_value(self):
#         value = random.choice(range(1, 100))
#         self.__value = value
#
# for obj in MyIterable(5):
#     print(obj)

# -----------------------------------------
#
# from faker import Faker
# from datetime import time
#
# faker = Faker()
#
#
# def user_generator(num_of_users: int):
#     for i in range(num_of_users):
#         user = {"id": random.randint(1, 10000), "name": faker.name(), "age": random.choice(range(1, 99))}
#         yield user
#
#
# users = user_generator(2)
# for user in users:
#     print(user)

# -----------------------------------------
# import time
# import random
#
# def retry(num_of_retries:int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             current_retries = 0
#             while current_retries < num_of_retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Cannot run function with exception {e}")
#                     current_retries += 1
#                     time.sleep(3)
#             raise Exception("Limit reached")
#         return wrapper
#     return decorator
#
# @retry(3)
# def send_fake_request():
#     randomizer = random.randint(5,20)
#     if randomizer < 8:
#         return True
#     else:
#         raise TimeoutError
#
# print(send_fake_request())
# -----------------------------------------
#
# import requests
# import json
# from assertpy import soft_assertions, assert_that
# from curlify import to_curl
#
# swapi_url = 'https://swapi.dev/api/people'
# request_params = {"search": "re",
#                   "page" : 1}
#
# response = requests.get(swapi_url, params=request_params)
# curl = to_curl(response.request)
# print(curl)
#
#
# print(response.status_code)
# print(response.json())
#
# with open('api_response.json', mode='w') as file:
#     json.dump(response.json(), file, indent=4)

# for user in response.json()['results']:
#     print(user['name'])
#
# def test_search_param():
#     with soft_assertions():
#         for user in response.json()['results']:
#             assert_that(user['name'],
#                         f'User {user['name']} returned incorrectly! '
#                         ).contains('bba')

# -----------------------------------------
import time
from datetime import datetime, timedelta

current_time_str = time.time()
print(time.ctime(current_time_str))

print(datetime.now())
diff = timedelta(days=3, hours=2)
print(datetime.now() - diff)
# print(time.strftime('%Y - %m - %d : %z', time.localtime()))
# -----------------------------------------
