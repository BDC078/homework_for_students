from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def cycle(obj: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь."""
    while True:
        for value in obj:
            yield value


class Cycle:

    def __init__(self, obj: Iterable[T]):
        self.obj = tuple(obj)
        self.length = len(tuple(obj))
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            self.index = 1
            return self.obj[0]
        else:
            res = self.obj[self.index]
            self.index += 1
            return res