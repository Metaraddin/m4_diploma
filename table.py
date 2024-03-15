import random
from typing import TypedDict, Unpack, Required, List
from base_class import BaseClass
from field import Field
from field_types.integer import Integer


class TableParams(TypedDict, total=False):
    name: Required[List[str] | str]
    pk_field: List[Field] | Field
    static_fields: List[Field] | Field
    dynamic_fields: List[Field] | Field
    dynamic_fields_count: List[int] | int


class Table(BaseClass):
    def __init__(self, **params: Unpack[TableParams]) -> None:
        super().__init__()
        self._wrap_values_in_lists(params)

        # check required
        if not params.get('name'):
            raise ValueError('Name is required')
        self._params = {'name': params.get('name')}
        self._randomize_params()

        pk_field = random.choice(params.get('pk_field')) if params.get('pk_field') else Field(name='id', type=Integer(autoincrement=True))
        pk_field.make_pk()

        self.fields = [pk_field]

        # static_fields
        if params.get('static_fields'):
            self.fields += params.get('static_fields')
        
        # dynamic_fields
        if params.get('dynamic_fields'):
            if params.get('dynamic_fields_count'):
                if max(params.get('dynamic_fields_count')) > len(params.get('dynamic_fields')):
                    ValueError('dynamic_fields_count must be less than the length of dynamic_fields')
                dynamic_fields_count = random.choice(params.get('dynamic_fields_count'))
            else:
                dynamic_fields_count = random.randint(0, len(params.get('dynamic_fields')))
            self.fields += random.sample(params.get('dynamic_fields'), dynamic_fields_count)

        self.fk_fields = []

    def as_dict(self):
        result = super().as_dict()
        result['fields'] = [i.as_dict() for i in self.fields]
        return result
