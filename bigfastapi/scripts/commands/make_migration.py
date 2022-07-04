import argparse
import os
from datetime import datetime

from dotenv import load_dotenv

from bigfastapi.core.Command import Command
from ..print_colors import bcolors

load_dotenv('.env')

MIGRATIONS_FOLDER = os.environ.get("MIGRATIONS_FOLDER")


def to_camel_case(snake_str: str) -> str:
    snake_str = snake_str.lower()
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0].title() + ''.join(x.title() for x in components[1:])


class MakeMigrationHelper(Command):

    def run(self, args: list = None):
        update = False
        parser = argparse.ArgumentParser(description="Create a migration file")
        parser.add_argument('migration_name', help='Name of migration file',
                            type=str)
        parser.add_argument('table_name', help='Table name',
                            type=str)
        parser.add_argument('-u', '--update', help='Set update flag', action="store_true")
        args = parser.parse_args(args)

        if args.update:
            update = True

        now = datetime.now()
        migration_name = args.migration_name.strip()
        table_name = args.table_name.strip()
        class_name = to_camel_case(migration_name)
        if update:
            contents = '''from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class ''' + class_name + ''':

    def up_schema(self, table: Blueprint):
        table.string('column_name')
        
    def down_schema(self, table: Blueprint):
        table.drop('column_name')

    def up(self):
        Schema.update(table_name="''' + table_name + '''", schema=self.up_schema)

    def down(self):
        Schema.update(table_name="''' + table_name + '''", schema=self.down_schema)
'''
        else:
            contents = '''from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class ''' + class_name + ''':

    def schema(self, table: Blueprint):
        table.id()

    def up(self):
        Schema.create(table_name="''' + table_name + '''", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="''' + table_name + '''")
'''
        file_name = "_" + str(now.year) + '_' + str(now.month).zfill(2) + '_' + str(now.day).zfill(2) + '_' + str(
            now.hour).zfill(2) + str(now.minute).zfill(2) + str(now.second).zfill(2) + '_' + migration_name + '.py'
        file = open(MIGRATIONS_FOLDER + file_name, 'a')
        file.write(contents)
        print(bcolors.OKGREEN + "Migration file " + MIGRATIONS_FOLDER + file_name + ' created')
