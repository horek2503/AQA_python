# Задача 1:
# Є 3 групи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist.
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)
australia_blacklist = {'Stepan', 'Olena', 'Vitaliy', 'Eugene'}
poker_blacklist = {'Dmytro', 'Maryna', 'Vitaliy', 'Eugene', 'Ihor', 'Oleh'}
alcohol_blacklist = {'David', 'Olena', 'Vitaliy', 'Alex'}
### option 1 -- set comprehension
# winners = {person for person in australia_blacklist if person in poker_blacklist and person in poker_blacklist and person in alcohol_blacklist}

### option 2 -- sets intersection
winners = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print('Task01:')
print(winners)

# Задача 2:
# Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Apartments', 'Oleh': 'Trench'}
# Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера.
# Використовувати цикл
person_apartments = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Apartments', 'Oleh': 'Trench'}
print('\nTask02:')
for person in person_apartments:
    print(f'{person} is living in {person_apartments[person]}')

# Задача 3:
# Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Вивести ТІЛЬКИ коректні імена(тобто стрінги).
# Використовувати Continue.
input_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
print('\nTask03:')
for item in input_list:
    if not isinstance(item, str):
        continue
    print(item)

# Задача 4:
# Порахувати та вивести(print) кількість букв в строці:
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
# Прикдад:
# Юзер вводить: My name is Emmy Santiago.
# Ви прінтаете щось на кшталт:M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне, що б чітко було зрозуміло скільки разів зустрічаеться кожна буква)
# Тобто кожну букву та скільки разів вона зустрічаеться
print('\nTask04:')
user_string = input('Please enter a string: ')
unique_symbols = list(set(user_string))
unique_symbols.sort()
for symbol in unique_symbols:
    print(f'"{symbol}" = {user_string.count(symbol)}')

# Задача 5
# Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічаеться у списку
# Умови:По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# Не використовувати методи/функції/класи
task_05_list = ['Me', 'show', 109, 90, 'po', False, 23, 'support', 289, 457]
print('\nTask05:')
for index in range(len(task_05_list)):
    if task_05_list[index] is not None and index != len(task_05_list) - 1:
        continue
    elif task_05_list[index] is None:
        break
    print("There is no None")

# Задача 6
# Вирішити задачу 4 без словника за 2 строки:
# 1 строка це input
# 2 строка це рішення
task_06_input = input("\nTask_06:\nInput your string:")
print(*[f'"{x}" = {task_06_input.count(x)}' for x in set(task_06_input)], sep='\n')
