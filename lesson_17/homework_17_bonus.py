import random
import time


def set_min_function_execution_time(min_execution_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            wrapper_added_time = 0
            if execution_time < min_execution_time:
                wrapper_added_time = min_execution_time - execution_time
                time.sleep(wrapper_added_time)
            print(
                f"Original function execution time: {round(execution_time, 2)}s. Added by wrapper: {round(wrapper_added_time, 2)}s")
            return result

        return wrapper

    return decorator


@set_min_function_execution_time(15)
def random_sleep_function(max_sleep_seconds):
    time_to_sleep = random.randint(1, max_sleep_seconds)
    time.sleep(time_to_sleep)
    return "Function completed"


print(random_sleep_function(20))
