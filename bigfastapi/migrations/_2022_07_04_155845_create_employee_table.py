from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class CreateEmployeeTable:

    def schema(self, table: Blueprint):
        table.id()
        table.string('name',255)
        table.boolean('true')

    def up(self):
        Schema.create(table_name="employees", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="employees")
