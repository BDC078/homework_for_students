from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for iter in iterables:
        for elem in iter:
            yield elem

class Chain:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0 or self.index >= len(self.iterables):
            raise StopIteration
        else:
            res = self.iterables[self.index]
            self.index += 1
            return res