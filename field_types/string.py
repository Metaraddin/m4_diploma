import random
from typing import TypedDict, Unpack, List
from type_base_class import TypeBaseClass


class StringParams(TypedDict, total=False):
    length: List[int] | int
    min_length: List[int] | int
    max_length: List[int] | int


class String(TypeBaseClass):
    def __init__(self, **params: Unpack[StringParams]) -> None:
        super().__init__()
        if not params:
            params = StringParams(
                length=random.choice([[], list(range(10, 51))]),
                min_length=random.choice([[], list(range(10, 31))]),
                max_length=random.choice([[], list(range(31, 51))]),
            )
        self._wrap_values_in_lists(params)

        # length
        if params.get('length'):
            self._params['length'] = params.get('length')
        else:
            # min and max length
            for param in ['min_length', 'max_length']:
                if value := params.get(param):
                    self._params[param] = value
            # min and max length validate
            if (self._params.get('min_length') and self._params.get('max_length')
                    and max(self._params['min_length']) > min(self._params['max_length'])):
                raise ValueError('max_length must be greater than min_length')

        self._randomize_params()
