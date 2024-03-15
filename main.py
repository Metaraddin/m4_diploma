from field_types.string import String
from field_types.integer import Integer
from field_types.boolean import Boolean
from field import Field
from table import Table
from pprint import pprint
from db import DataBase, RelationType


t1 = Table(
    name=['table1', 'table2'],
    static_fields=Field(name=['login', 'full_name'], type=String()),
    dynamic_fields=[
        Field(name=['dyn11', 'dyn12', 'dyn13'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn21', 'dyn22', 'dyn23'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn31', 'dyn32'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn4'], type=[String(), Integer(), Boolean()]),
        Field(name='dyn5', type=[String(), Integer(), Boolean()])
    ],
    dynamic_fields_count=5
)

t2 = Table(
    name='table2',
    static_fields=Field(name=['login', 'full_name'], type=String()),
    dynamic_fields=[
        Field(name=['dyn11', 'dyn12', 'dyn13'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn21', 'dyn22', 'dyn23'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn31', 'dyn32'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn4'], type=[String(), Integer(), Boolean()]),
        Field(name='dyn5', type=[String(), Integer(), Boolean()])
    ],
    dynamic_fields_count=5
)

t3 = Table(
    name='table3',
    static_fields=Field(name=['login', 'full_name'], type=String()),
    dynamic_fields=[
        Field(name=['dyn11', 'dyn12', 'dyn13'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn21', 'dyn22', 'dyn23'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn31', 'dyn32'], type=[String(), Integer(), Boolean()]),
        Field(name=['dyn4'], type=[String(), Integer(), Boolean()]),
        Field(name='dyn5', type=[String(), Integer(), Boolean()])
    ],
    dynamic_fields_count=range(1, 5)
)

db = DataBase()
db.add_table([t1, t2, t3])
# pprint(db.as_dict())

db.add_relation(RelationType.one_to_one, 'table1', 'table2')
db.add_relation(RelationType.one_to_many, 'table1', 'table3')
db.add_relation(RelationType.many_to_many, 'table2', 'table3')
pprint(db.as_dict())