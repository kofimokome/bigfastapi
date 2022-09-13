from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class UpdateEmployeeTable:

    def up_schema(self, table: Blueprint):
        table.string('new_one', 200)
        table.rename('name', 'new_name')

    def down_schema(self, table: Blueprint):
        table.drop('new_one')
        table.rename('new_name', 'name')

    def up(self):
        Schema.update(table_name="employees", schema=self.up_schema)

    def down(self):
        Schema.update(table_name="employees", schema=self.down_schema)
