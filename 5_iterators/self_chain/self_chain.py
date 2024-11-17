from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def chain(*iterables: Iterable[T]) -> Generator[T, None, None]:
    """Пишите ваш код здесь"""
    for iter in iterables:
        for elem in iter:
            yield elem

class Chain:
    def __init__(self, *iterables: Iterable[T]):
        """Реализуйте класс ниже"""
        self.iter = iterables

    def __iter__(self):
        for iter in self.iter:
            for elem in iter:
                yield elem

    def __next__(self):
        return self