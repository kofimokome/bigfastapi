from .Blueprint import Blueprint
from .DB import DB


class Schema:

    @staticmethod
    def create(table_name: str, schema):
        table = Blueprint()
        schema(table=table)
        connection = DB.get_cursor()
        print(table.to_string())
        query = "CREATE TABLE IF NOT EXISTS `" + table_name + '` (' + table.to_string() + ')'

        connection.execute(query)
        connection.close()

    @staticmethod
    def update(table_name: str, schema):
        table = Blueprint(is_update=True)
        schema(table=table)
        columns = table.get_columns()
        for column in columns:
            connection = DB.get_cursor()
            query = "ALTER TABLE `" + table_name + '`' + column.to_string()
            print(query)

            connection.execute(query)
            connection.close()

    @staticmethod
    def dropIfExist(table_name: str):
        query = "DROP TABLE `" + table_name + '`'
        connection = DB.get_cursor()

        connection.execute(query)
        connection.close()
