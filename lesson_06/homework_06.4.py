"""
Є ліст з числами, порахуйте суму усіх ПАРНИХ чисел в цьому лісті
"""
source_list = [3, 6, 20, 11, 4, 18, 9, 35, 17, 12, 8, 13, 99, 40]
sum_of_even_numbers = sum([number for number in source_list if number % 2 == 0])
print(f"Sum of even numbers from source list = {sum_of_even_numbers}")
