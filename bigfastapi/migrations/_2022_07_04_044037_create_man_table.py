from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class CreateManTable:

    def schema(self, table: Blueprint):
        table.id()

    def up(self):
        Schema.create(table_name="man", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="man")
