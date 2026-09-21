def get_even_numbers_till_n(n: int):
    if n > 0:
        for number in range(n + 1):
            if number % 2 == 0:
                yield number


def get_fibonacci_numbers_till_n(n: int):
    if n >= 0:
        pre_previous_number = 0
        previous_number = 0
        current_number = 0

        while current_number <= n:
            if current_number == 0:
                yield 0
                current_number = 1
            elif current_number == 1 and previous_number == 0:
                yield 1
                previous_number = 1
            else:
                current_number = previous_number + pre_previous_number
                pre_previous_number = previous_number
                previous_number = current_number
                if current_number <= n:
                    yield current_number


evens = get_even_numbers_till_n(8)
print("Generating even numbers:")
for number in evens:
    print(number)

fibonacci_list = get_fibonacci_numbers_till_n(21)
print("Generating Fibonacci numbers:")
for i in fibonacci_list:
    print(i)
