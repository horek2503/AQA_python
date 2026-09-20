class IteratorByReversedList:
    def __init__(self, input_list: list):
        self.__list = input_list
        self.__length = len(input_list)
        self.__reversed_list = input_list[::-1]
        self.__current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index < self.__length:
            value = self.__reversed_list[self.__current_index]
            self.__current_index += 1
            return value
        else:
            raise StopIteration


class IterateByEvenNumbers:
    def __init__(self, n: int):
        self.__max_value = n
        self.__current_value = 0

    def __iter__(self):
        return (self)

    def __next__(self):
        if self.__current_value > self.__max_value:
            raise StopIteration
        result = self.__current_value
        self.__current_value += 2
        return result


my_iter_reverse_list = IteratorByReversedList([9, 8, 77, 15, 7])
print("Iterating through reverse list values:")
for element in my_iter_reverse_list:
    print(element)

my_iter_even_numbers = IterateByEvenNumbers(8)
print("Iterating through reverse list values:")
for element in my_iter_even_numbers:
    print(element)
