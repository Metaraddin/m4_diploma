from typing import TypedDict, Unpack, Type, Required, List
from base_class import BaseClass
from type_base_class import TypeBaseClass


class FieldParams(TypedDict, total=False):
    unique: List[bool] | bool
    not_null: List[bool] | bool
    type: Required[List[Type[TypeBaseClass]] | Type[TypeBaseClass]]
    name: Required[List[str] | str]


class Field(BaseClass):
    def __init__(self, **params: Unpack[FieldParams]):
        super().__init__()
        self._wrap_values_in_lists(params)
        # check required
        for param in ['type', 'name']:
            if not params.get(param):
                raise ValueError(f'{param} is required')
        if not params.get('not_null'):
            params['not_null'] = [True, False]
        self._params = params
        self._randomize_params()
        self.params['pk'] = False
        self.params['fk'] = False

    def make_pk(self):
        self.params['pk'] = True
        self.params['not_null'] = True
        self.params['unique'] = True

    def make_fk(self, table_name: str):
        self.params['fk'] = True
