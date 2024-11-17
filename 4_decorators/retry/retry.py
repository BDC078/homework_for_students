# реализуйте декоратор вида @retry(count: int, delay: timedelta, handled_exceptions: tuple[type(Exceptions)])
import time
from datetime import timedelta


def retry(count, delay, handled_exceptions = Exception):
    if count < 1:
        raise ValueError
    def decorator(func):
        def wrapper(*args, **dict):
            for i in range(count):
                try:
                    return func(*args, **dict)
                except handled_exceptions:
                    if i + 1 == count:
                        raise
                time.sleep(delay.total_seconds())
        return wrapper
    return decorator
