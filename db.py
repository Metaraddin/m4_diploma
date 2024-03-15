from typing import List, Dict
from enum import Enum
from table import Table


class RelationType(Enum):
    one_to_one = 1
    one_to_many = 2
    many_to_many = 3


class DataBase():
    def __init__(self):
        self.tables: Dict[str, Table] = {}

    def add_table(self, table: List[Table] | Table):
        if type(table) is list:
            for i in table:
                self.tables[i.params['name']] = i
        elif type(table) is Table:
            self.tables[table.params['name']] = table

    def add_relation(self, relation_type: RelationType,  name_left_table: str, name_right_table: str):
        left_pks = [i for i in self.tables[name_left_table].fields if i.params['pk']]
        right_pks = [i for i in self.tables[name_right_table].fields if i.params['pk']]

        for i in left_pks + right_pks:
            i.params['fk'] = True
            if i.params['type'].params.get('autoincrement'):
                i.params['type'].params['autoincrement'] = False

        for i in left_pks:
            i.params['name'] = name_left_table + '.' + i.params['name']

        for i in right_pks:
            i.params['name'] = name_right_table + '.' + i.params['name']

        if relation_type is RelationType.one_to_one:
            for i in left_pks:
                i.params['pk'] = False
                i.params['unique'] = True
            self.tables[name_right_table].fields += left_pks
        elif relation_type is RelationType.one_to_many:
            for i in left_pks:
                i.params['pk'] = False
                i.params['unique'] = False
            self.tables[name_right_table].fields += left_pks
        elif relation_type is RelationType.many_to_many:
            for i in left_pks + right_pks:
                i.params['pk'] = True
                i.params['unique'] = False
            table_name = self.tables[name_left_table].params['name'] + self.tables[name_right_table].params['name']
            self.tables[table_name] = Table(
                name=table_name,
                static_fields=left_pks + right_pks
            )

    def as_dict(self):
        return {name: table.as_dict() for name, table in self.tables.items()}
