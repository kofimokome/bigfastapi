from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class Tesing():

    def schema(self, table: Blueprint):
        table.id()

    def up(self):
        Schema.create(table_name="mem", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="mem")
