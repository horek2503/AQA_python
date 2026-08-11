class Student:

    def __init__(self, first_name, second_name, age:int, avg_score:float=0):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.__avg_score = avg_score

    def recalculate_avg_score(self, classes_and_scores:dict = {}):
        if len(classes_and_scores) != 0:
            self.__avg_score = round(sum(classes_and_scores.values())/len(classes_and_scores.items()), 2)
        else:
            print(f"WARNING: Average score is not updated for student {self.first_name} {self.second_name} as no data provided!")

    def get_info(self):
        print(f"Student {self.first_name} {self.second_name} is {self.age} years old and has average score {self.__avg_score}")

student_1 = Student('Mykhaylo', 'Ovcharenko', age = 22, avg_score = 100)
student_1.get_info()

print(f"Re-calculating average score for {student_1.first_name} {student_1.second_name}...")
student_1.recalculate_avg_score({'Math': 95, 'History': 100, 'Literature': 80, 'Philosophy': 75})
student_1.get_info()