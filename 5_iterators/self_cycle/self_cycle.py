from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    while True:
        for value in obj:
            yield value

class Cycle:
    def __init__(self, obj: Iterable[T]):
        """Реализуйте класс"""
        self.obj = obj

    def __iter__(self):
        while True:
            for i in self.obj:
                yield i

    def __next__(self):
        return self