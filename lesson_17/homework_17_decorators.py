import logging
import functools
from definitions import LOGS_FOLDER
from pathlib import Path

hw17_logger = logging.getLogger()
hw17_logger.setLevel(logging.DEBUG)
log_path = Path(LOGS_FOLDER, 'hw17.log')
file_handler = logging.FileHandler(filename=log_path, mode='a', encoding='utf-8')
file_formatter = logging.Formatter('{asctime}: {levelname} - {message} ', style='{')
file_handler.setFormatter(file_formatter)
hw17_logger.addHandler(file_handler)


def log_function_arguments_and_results(f):
    @functools.wraps(f)
    def wrapper_log(*args, **kwargs):
        result = f(*args, **kwargs)
        hw17_logger.info(
            f'Function "{f.__name__}" is called with arguments: {args if len(args) > 0 else ''}, {kwargs if len(kwargs) > 0 else ''}; result is {result}')
        return result

    return wrapper_log


def intercept_exceptions(f):
    @functools.wraps(f)
    def wrapper_intercept(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            hw17_logger.info(
                f'Function "{f.__name__}" is called with arguments: {args if len(args) > 0 else ''}, {kwargs if len(kwargs) > 0 else ''}, but caused an exception "{e}"')

    return wrapper_intercept


@intercept_exceptions
@log_function_arguments_and_results
def divide_a_by_b(a, b):
    return a / b


print(divide_a_by_b(6, 3))
print(divide_a_by_b(a=6, b=0))
