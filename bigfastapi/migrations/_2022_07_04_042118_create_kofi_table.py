from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class CreateKofiTable:

    def schema(self, table: Blueprint):
        table.id()

    def up(self):
        Schema.create(table_name="kofi", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="kofi")
