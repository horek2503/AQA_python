"""
1) Опишіть клас Вагон
2) Вагон повинен містити список пасажирів і дозволяти додавати пасажирів
3) У Вагоні може бути не більше 10 пасажирів
4) Під час використання функції len у вагоні я хочу бачити кількість пасажирів
5) Кожен вагон повинен мати номер
6) Опишіть об’єкт «Поїзд»
7) Клас повинен містити поля та метод для додавання вагонів(необхідно додати об’єкти та екземпляри класу вагонів)
8) В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
9) Використовуючи len у поїзді, я хочу бачити кількість вагонів без локомотива
"""

class Carriage:
    def __init__(self, carriage_number:int, passengers: list = None):
        self.carriage_number = carriage_number
        self.passengers = passengers or []

    def __setattr__(self, key, value):
        if key == 'passengers':
            # Basic validation for passenger list
            Carriage.validate_added_passengers(value)
            if self.carriage_number == 0 and value != []:
                raise ValueError("Locomotive cannot have passengers!")
            if len(value) > 10:
                raise ValueError("Passengers number cannot exceed 10 in one carriage!")
        self.__dict__[key] = value

    def add_passengers(self, value: list[str]):
        # Basic validation for passenger list
        Carriage.validate_added_passengers(value)
        self.passengers += value

    @staticmethod
    def validate_added_passengers(passenger_list:list):
        if not isinstance(passenger_list, list):
            raise ValueError("'Passengers' must be provided as a list!")
        for person in passenger_list:
            if not (isinstance(person, str) and person != ''):
                raise ValueError("Each person name must be a non-empty string!")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f'Carriage {self.carriage_number} contains {len(self)} passengers: {self.passengers}'

class Train:
    def __init__(self, name, carriages:list[Carriage] = None):
        self.name = name
        self.carriages = carriages or []

    def __setattr__(self, key, value):
        if key == 'carriages':
            if not (isinstance(value, list) or all(isinstance(element, Carriage) for element in value)):
                raise ValueError("'Carriages' must be a list of carriages!")

            # Check if locomotive exists in carriage list, if not - add.
            carriage_numbers = [carriage.carriage_number for carriage in value]
            if 0 not in carriage_numbers or value == []:
                value.insert(0, Carriage(carriage_number = 0))

            # Check if all carriage numbers inside the train are unique.
            for carriage_number in carriage_numbers:
                if carriage_numbers.count(carriage_number) > 1:
                    raise ValueError(f"Carriage numbers must be unique! Duplicates found for carriage #{carriage_number}")
        self.__dict__[key] = value

    def add_carriages(self, carriages:list):
        if (not isinstance(carriages, list)
                or carriages == []
                or any(not isinstance(carriage, Carriage) for carriage in carriages)):
            raise ValueError("You can add only a non-empty list of carriages!")
        self.carriages += carriages

    def __len__(self):
        return len(self.carriages) - 1

    def __str__(self):
        return f'Train "{self.name}" has {len(self)} carriages for passengers.'


first_carriage_passengers = ['Sam', 'Olha', 'Ira', 'Oleh', 'Tolik', 'Den', 'Anna', 'Stefa', 'Jack', 'Bob']
train_Odesa_Lviv = Train(name='12(West Express): Odesa - Lviv', carriages = [Carriage(carriage_number=4, passengers=first_carriage_passengers)])
train_Odesa_Lviv.add_carriages([Carriage(carriage_number=3,  passengers=['Mike', 'Tima'])])
train_Odesa_Lviv.add_carriages([Carriage(carriage_number=2,  passengers=['Ivan', 'Petro'])])

print(train_Odesa_Lviv)

for carriage in train_Odesa_Lviv.carriages:
    print(carriage)
