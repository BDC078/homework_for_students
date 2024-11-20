from typing import Generator, Iterable, TypeVar

T = TypeVar("T")


def batched(obj: Iterable[T], n: int) -> Generator[tuple[T], None, None]:
    """Пиши свой код здесь."""
    for i in range(0, len(obj), n):
        yield tuple(obj[i:i + n])

class Batched:
    def __init__(self, obj: Iterable[T], n: int):
        """Реализуй этот класс."""
        self.object = obj
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.object):
            raise StopIteration
        else:
            batch = tuple(self.object[self.index : self.index + self.n])
            self.index += self.n
            return batch