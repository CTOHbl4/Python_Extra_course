from typing import Protocol, Sized, Sequence, Callable, Any
from abc import abstractmethod


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, value: Any) -> bool: ...


Sizeable = Sized

Sortable = Sequence[Comparable]


def defkey(element: Comparable) -> Comparable:
    if isinstance(element, Sizeable):
        return len(element)
    return element


def strictsort(seq: Sortable, key: Callable[[Comparable], Comparable] = defkey) -> Sortable:
    return sorted(seq, key=key)


c: Sortable = [6, 1, 4, 2, 7, 2, 8, 3]
print(*strictsort(c))
print(*strictsort([6., 1., 4., 2., 7., 2., 8., 3.]))
print(*strictsort(["234", "sdf23452345234gg", "45645674567", "ASDASD"]))
print(*strictsort([(1, 2, 4, 9), (2, 7, 4, 6, 8), (1,), (8, 9, 23), (7, 2, 1)]))
print(defkey(9), defkey("999"))

# c1: Sortable = [7j, 2j, 3j]
# defkey(iter("123"))
# print(*strictsort({1: 2, 3: 4}))
