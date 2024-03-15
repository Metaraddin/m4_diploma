from typing import TypedDict, Unpack, Required


class Kwargs(TypedDict):
    a: Required[int]
    b: Required[int]


class Test:
    def __init__(self, kwargs: Kwargs) -> None:
        pass

