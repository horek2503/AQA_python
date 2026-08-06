# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    max_result = 25
    # Initialize the appropriate variable
    multiplier = 1
    # Complete the while loop condition.
    while multiplier <= 9:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > max_result:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1

print("# task 1:")
multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(num1, num2):
    return num1 + num2

print("\n# task 2:")
print(sum_of_two_numbers(3, 9))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_of_numbers(input_list:list):
    return sum(input_list) / len(input_list)
numbers = [9, 14, 12, 31]
print("\n# task 3:")
print(f"Average of {numbers} is {avg_of_numbers(numbers)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(source_string:str):
    return source_string[::-1]

string_for_task_4 = "abcdefghijkl"
print("\n# task 4:")
print(f'Reversed value of "{string_for_task_4}" is "{reverse_string(string_for_task_4)}"')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_str_in_list(input_list:list):
    return max(input_list, key=len)

list_for_task_5 = ['Some', 'of', 'these', 'words', 'is', 'longer']
longest_from_list = find_longest_str_in_list(list_for_task_5)
print("\n# task 5:")
print(f'The longest from source list is "{longest_from_list}"')

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    # Check if str2 is included to str1; if yes - return index; if not - return -1
    if str2 in str1:
        return str1.index(str2)
    return -1

print("\n# task 6:")
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def return_only_strings_from_list(source_list:list):
    return [element for element in source_list if isinstance(element, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print("\n# task 7:")
print("Strings from source list:")
print(return_only_strings_from_list(lst1))

# task 8
def filter_cars_by_criteria(cars:dict, max_price:int, min_engine: float, min_year:int):
    # input data format:
    #           {'model': ('color', year, engine, 'type', price)}

    filtered_cars = {key: value for key, value in cars.items()
                     if value[1] >= min_year
                     and value[2] >= min_engine
                     and value[4] <= max_price
                     }
    return filtered_cars

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000)
}

cars_for_me = filter_cars_by_criteria(car_data, max_price=50000, min_year=2018, min_engine=2.0)
print("\n# task 8:")
print("Cars matching my criteria:")
print(cars_for_me)

# task 9
def remove_extra_spaces_from_text(input_text: str):
    # First remove extra spaces in the beginning and in the end of text
    target_text = input_text.strip()
    # Remove more than one space in sequence
    while "  " in target_text:
        target_text = target_text.replace("  ", " ")
    return target_text

text_for_task9 = """
  So    many strange   things can happen while        learning Python!          """
print("\n# task 9:")
print(remove_extra_spaces_from_text(text_for_task9))

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

def count_gas_station_visits_in_trip(distance, fuel_consumption, tank):
    # Calculate needed fuel amount
    total_fuel_needed = distance / 100 * fuel_consumption
    # Calculate min number of gas station visits
    if total_fuel_needed % tank:
        gas_station_visits = int(total_fuel_needed // tank + 1)
    else:
         gas_station_visits =int(total_fuel_needed // tank)
    print(f"Your trip requires at least {gas_station_visits} gas station visits")

print("\n# task 10:")
count_gas_station_visits_in_trip(distance=2000, fuel_consumption=12, tank=65)