import random
from typing import TypedDict, Unpack, List
from type_base_class import TypeBaseClass


class IntegerParams(TypedDict, total=False):
    autoincrement: List[bool] | bool
    min_value: List[int] | int
    max_value: List[int] | int


class Integer(TypeBaseClass):
    def __init__(self, **params: Unpack[IntegerParams]) -> None:
        super().__init__()
        if not params:
            params = IntegerParams(
                autoincrement=random.choice([[], [True, False]]),
                min_value=random.choice([[], list(range(100))]),
                max_value=random.choice([[], list(range(100, 10**5))]),
            )
        self._wrap_values_in_lists(params)

        # length
        if params.get('autoincrement'):
            self._params['autoincrement'] = params.get('autoincrement')
        else:
            # min and max length
            for param in ['min_value', 'max_value']:
                if value := params.get(param):
                    self._params[param] = value
            # min and max length validate
            if (self._params.get('min_value') and self._params.get('max_value')
                    and max(self._params['min_value']) > min(self._params['max_value'])):
                raise ValueError('max_value must be greater than min_value')

        self._randomize_params()
