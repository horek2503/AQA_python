import pytest
from assertpy import soft_assertions, assert_that
from homework_12 import get_car_data, count_gas_station_visits_in_trip


def test_car_data_not_empty():
    car_list = get_car_data()
    assert len(car_list) > 0, f"Car data is empty!"


def test_car_data_is_dict():
    car_list = get_car_data()
    assert isinstance(car_list, dict), f"Car list is expected to be a dict, but got: {type(car_list)}"


def test_validate_car_data_format():
    car_list = get_car_data()
    with soft_assertions():
        for car, params in car_list.items():
            # Validate keys (ER: non-empty string)
            assert_that(car, f"'{car}' car key is expected to be NOT None!").is_not_none()
            if car is not None:
                assert_that(car, f"'{car}' car key is expected to be a string, but got {type(car)}!").is_instance_of(
                    str)
                if type(car) is str:
                    assert_that(car, f"'{car}' car key is expected to be NOT empty!").is_not_empty()
            # Validate values (ER: tuple with 5 elements)
            assert_that(params, f"Params for '{car}' expected to be a tuple, but got {type(params)}!").is_instance_of(
                tuple)
            if isinstance(params, tuple):
                assert_that(params, f"'{car}' must have 5 params, but got {len(params)}!").is_length(5)


def test_validate_params_for_each_car():
    expected_car_format = {'color': str, 'year': int, 'engine': float, 'body_type': str, 'price': int}
    expected_car_format_keys = list(expected_car_format.keys())
    expected_car_format_values = list(expected_car_format.values())

    car_list = get_car_data()
    with soft_assertions():
        for car, params in car_list.items():
            with soft_assertions():
                if len(params) == len(expected_car_format):
                    for i in range(len(expected_car_format)):
                        assert_that(params[i],
                                    f"Error for '{car}' car: '{expected_car_format_keys[i]}' is expected to have type {expected_car_format_values[i]}, but got: {type(params[i])}"
                                    ).is_type_of(expected_car_format_values[i])


@pytest.mark.parametrize('distance, fuel_consumption, tank, ER',
                         [(1000, 10, 50, 2),
                          (750, 8, 46, 2),
                          (1800, 12, 60, 4),
                          (0, 5, 50, 0)
                          ])
def test_count_gas_station_visits_in_trip_positive(distance, fuel_consumption, tank, ER):
    assert_that(count_gas_station_visits_in_trip(distance, fuel_consumption, tank),
                f"Wrong gas station visits calculation for input data set: {distance} - {fuel_consumption} - {tank}"
                ).is_equal_to(ER)


@pytest.mark.parametrize('distance, fuel_consumption, tank, expected_error_type',
                         [(None, 10, 50, TypeError),
                          (-50, 0, 46, ValueError),
                          (1800, 'some', 60, TypeError),
                          (0, -3, 50, ValueError),
                          (500, 8, None, TypeError),
                          (950, 7, -9, ValueError)
                          ])
def test_count_gas_station_visits_in_trip_negative(distance, fuel_consumption, tank, expected_error_type):
    expected_error_caught = False
    try:
        count_gas_station_visits_in_trip(distance, fuel_consumption, tank)
    except expected_error_type:
        expected_error_caught = True
    finally:
        assert expected_error_caught == True, f"Error type mismatch for iteration data:'{distance} -> ,{fuel_consumption} ->,{tank}'"
