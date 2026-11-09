import re
### ----------------------------------------------------------------------
"""INPUT PHONE NUMBER AND VALIDATE THE FORMAT"""
# user_phone = input('Enter your phone(format +380XX-YYYYYYY):')
# phone_format = r'^\+380[0-9]{2}-[0-9]{7}$'
#
# if re.match(phone_format, user_phone):
#     print("Phone number matches format!")
# else:
#     print("Wrong phone format!!!")
### ----------------------------------------------------------------------
"""
Умова:
- Напишіть функція, що перевіряє чи відповідає вимогам ім’я користувача.
- Ім’я користувача може містити літери латиницею, цифри і символ підкреслення, і мати довжину від 4 до 16 символів.
- Якщо введений рядок відповідає цим умовам, функція повертає **True** , якщо ні - **False**.
"""
#
# def validate_user_name(user_name:str):
#     name_format = r'^[a-zA-Z0-9_]{4,16}$'
#     return True if re.match(name_format, user_name) else False
### ----------------------------------------------------------------------
"""
Напишіть функцію, яка приймає дату, введену користувачем і перевіряє, чи ця дата у форматі "дд-мм-гггг" або “дд.мм.гггг”,
де розділення дати може бути крапкою або дефісом. Поверніть True, якщо дата валідна, та False, якщо ні.
"""
# def validate_date_format(input_date:str, format:str = None):
#
#     ### Option 1 - just regexp (no value validation)
#     ### ----------------------------------------------------------------------
#     # date_format_1 = r'[0-9]{2}-[0-9]{2}-[0-9]{4}'
#     # date_format_2 = r'[0-9]{2}\.[0-9]{2}\.[0-9]{4}'
#     # return True if re.match(date_format_1, input_date) or re.match(date_format_2, input_date) else False
#     ### ----------------------------------------------------------------------
#
#     ### Option 2 - values validation using datetime
#     ### ----------------------------------------------------------------------
#     from datetime import datetime
#     try:
#         datetime.strptime(input_date, format)
#     except ValueError:
#         return False
#     else:
#         return True
#     ### ----------------------------------------------------------------------
# print(validate_date_format('10.05.2026', '%d.%m.%Y'))
# print(validate_date_format('99-05-2026', '%d-%m-%Y'))
### ----------------------------------------------------------------------

source_text = """
Finally they found out that the night was going to catch them right in the middle of their way home.
"""
search_the = r'\b(the[\S]?)\b'
search_3_plus = r'\b([a-zA-Z]{3,})\b'
# Findall -> find all matches and returns a list of found values
print(re.findall(search_3_plus, source_text))
# search -> find groups; 0 - whole line; 1...n - each group
print(re.search(search_3_plus, source_text).group(0))


txt = "The rain in Spain is ai. Mr Been phone is +38093-1111111. His email is mrbean2@gmail.com"
# x = re.search("ai", txt)
# print(x) #this will print an object
# print(x.start()) #this will print an object position
# print(x.span()) #this will print an object position
# print(re.sub('ai','an', txt)) # substitute
# print(re.findall('rain|Spain', txt)) # OR operator
email_regex=  r'\b[\w]+@[a-zA-Z.]+'
phone_regex = r'\+\d{5}-\d{7}'
print(re.findall(email_regex, txt))
print(re.findall(phone_regex, txt))
