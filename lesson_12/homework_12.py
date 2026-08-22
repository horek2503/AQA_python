def get_car_data():
    return {
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

def count_gas_station_visits_in_trip(distance, fuel_consumption, tank):
    if not isinstance(distance, (int, float)):
        raise TypeError('Distance must be a number!')
    if distance < 0:
        raise ValueError('Distance must be positive!')
    if not isinstance(fuel_consumption, (int, float)):
        raise TypeError('Fuel consumption must be a number!')
    if not 0 > fuel_consumption < 100:
        raise ValueError('Incorrect fuel consumption!')
    if not isinstance(tank, (int, float)):
        raise TypeError('Tank must be a number!')
    if not 0 > tank < 100:
        raise ValueError('Incorrect tank value!')

    total_fuel_needed = distance / 100 * fuel_consumption
    if total_fuel_needed % tank:
        gas_station_visits = int(total_fuel_needed // tank + 1)
    else:
         gas_station_visits =int(total_fuel_needed // tank)
    return gas_station_visits

class Student:

    def __init__(self, first_name: str, second_name: str, age: int, avg_score: float = 0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.__avg_score = avg_score

    def __setattr__(self, key, value):
        if key in ('first_name', 'second_name'):
            if not isinstance(value, str):
                raise TypeError("Student name must be string!")
            if value == '':
                raise ValueError("Name cannot be empty!")
            self.__dict__[key] = value
        if key == 'age':
            if not isinstance(value, int):
                raise TypeError("Student age must be int!")
            if not 0 < value < 100:
                raise ValueError("Incorrect age!")
            self.__dict__[key] = value
        if key == '_Student__avg_score':
            if not isinstance(value, (int, float)):
                raise TypeError("Student average score must be int or float!")
            if not 0 <= value <= 100:
                raise ValueError("Incorrect average score!")
            self.__dict__[key] = value

    def recalculate_avg_score(self, classes_and_scores: dict = {}):
        if len(classes_and_scores) != 0:
            self.__avg_score = round(sum(classes_and_scores.values()) / len(classes_and_scores.items()), 2)
        else:
            print(
                f"WARNING: Average score is not updated for student {self.first_name} {self.second_name} as no data provided!")

    def get_info(self):
        return f"Student {self.first_name} {self.second_name} is {self.age} years old and has average score {self.__avg_score}"

    def get_avg_score(self):
        return self.__avg_score
