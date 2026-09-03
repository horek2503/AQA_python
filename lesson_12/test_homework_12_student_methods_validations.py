import pytest
from assertpy import soft_assertions, assert_that
from homework_12 import Student

@pytest.mark.parametrize('first_name, second_name, age, average_score',
                         [('Andrii', 'Ivanov', 26, 0),
                          ('Olena', 'Baranova', 29, 90)
                          ])
def test_student_create_positive(first_name, second_name, age, average_score):
    test_student = Student(first_name=first_name, second_name=second_name, age=age, avg_score=average_score)
    assert (
            test_student.first_name == first_name
            and test_student.second_name == second_name
            and test_student.age == age
            and test_student.get_avg_score() == average_score), \
        f"Student instance created incorrectly for '{first_name} {second_name}'"


@pytest.mark.parametrize('first_name, second_name, age, average_score, expected_error_type',
                         [(None, 'Ivanov', 26, 100, TypeError),
                          ('Olena', '', 29, 90, ValueError),
                          ('Tetyana', 0, 33, 80, TypeError),
                          (['Hanna'], 'Novikova', 30, 50, TypeError),
                          ('Maks', 'Ionov', -6, 90, ValueError),
                          ('Kyrylo', 'Getz', 0, 90, ValueError),
                          ('olha', 'Stop', 101, 90, ValueError),
                          ('Stepan', 'tiger', 24, -1, ValueError),
                          ('Iryna', 'Semenova', 50, 105, ValueError),
                          ('Petro', 'Shpak', 50, 'many', TypeError)
                          ])
def test_student_create_negative(first_name, second_name, age, average_score, expected_error_type):
    expected_error_caught = False
    try:
        test_student = Student(first_name=first_name, second_name=second_name, age=age, avg_score=average_score)
    except expected_error_type:
        expected_error_caught = True
    finally:
        assert expected_error_caught == True, f"Error type mismatch for iteration data:'{first_name} {second_name}'"


@pytest.mark.parametrize('lessons_and_marks, expected_score',
                         [({'Math': 95, 'History': 100, 'Literature': 80}, 91.67),
                          ({'Physics': 70, 'History': 95, 'Literature': 80, 'Drawing': 75, 'Chemistry': 80}, 80),
                          ({'Computer science': 95, 'Radiology': 88, 'Theoretical mechanics': 90, 'Physical trainings': 80, 'Chemistry': 60}, 82.6),
                          ])
def test_student_recalculate_avg_score(lessons_and_marks: dict, expected_score: int | float):
    test_student = Student('Ivan', 'Petrov', 30)
    test_student.recalculate_avg_score(lessons_and_marks)
    assert_that(test_student.get_avg_score()
                , "Wrong avg_score calculation for student {test_student.first_name} {test_student.second_name}"
                ).is_equal_to(expected_score)

def test_student_get_info_validation():
    test_data = {'first_name': 'Ivan', 'second_name': 'Petrov', 'age': 38, 'avg_score': 78}
    test_student = Student(**test_data)
    get_info_result = test_student.get_info()
    for keyword in test_data.values():
        assert str(keyword) in get_info_result, f'"{keyword}" value from test Student instance is NOT met in get_info() result!'
