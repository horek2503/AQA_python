"""
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try / except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""
test_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "90,8,1,7,12,spaceX"]

def sum_of_numbers_from_list_of_strings(input_data:list[str]):
    for iteration_data in test_data:
        result = f"Сума чисел {iteration_data} = "
        try:
            separated_string = iteration_data.split(',')
            numbers = [int(x) for x in separated_string]
        except ValueError as e:
            result += f"Не можу це зробити!\n\t {e}"
        except Exception:
            result += "Something went wrong..."
        else:
            result += str(sum(numbers))
        finally:
            print(result)

sum_of_numbers_from_list_of_strings(test_data)