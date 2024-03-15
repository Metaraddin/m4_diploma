import random
from typing import TypedDict, Unpack
from type_base_class import TypeBaseClass


class BooleanParams(TypedDict, total=False):
    pass


class Boolean(TypeBaseClass):
    def __init__(self, **params: Unpack[BooleanParams]) -> None:
        super().__init__()
        # if not params:
        #     params = BooleanParams()
        self._wrap_values_in_lists(params)
        self._randomize_params()
