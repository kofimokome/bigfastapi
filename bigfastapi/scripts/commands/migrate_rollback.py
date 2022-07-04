# from ...migrations import *
import importlib.util
import os
import sys

from dotenv import load_dotenv

from bigfastapi.core.Command import Command
from bigfastapi.core.DB import DB
from .utils import create_migrations_table, get_db_migrations, get_max_batch_number
from ..print_colors import bcolors

load_dotenv('.env')

MIGRATIONS_FOLDER = os.environ.get("MIGRATIONS_FOLDER")


class MigrateRollBackHelper(Command):

    def run(self, args: list = None):
        try:
            create_migrations_table()
        except Exception:
            pass

        db_migration_files = get_db_migrations()
        # print("to migrate is ", files_to_migrate)
        batch_number = get_max_batch_number()
        if batch_number is None:
            batch_number = 1

        db_migration_files = [x[1] for x in db_migration_files if x[2] == batch_number]
        if len(db_migration_files) == 0:
            print(bcolors.OKGREEN + "Migration files are up to date " + bcolors.ENDC)
        else:
            db_migration_files.sort()
            db_migration_files.reverse()
            for migration_file in db_migration_files:
                file_name = migration_file
                print(bcolors.WARNING + "Rolling back " + file_name + bcolors.ENDC)
                function_name = file_name.split('_')
                function_name = [x.title() for x in function_name if not x.isnumeric()]
                function_name = ''.join(function_name)
                # module = importlib.import_module('migrations.' + file_name, function_name)
                spec = importlib.util.spec_from_file_location("migrations", MIGRATIONS_FOLDER + migration_file + ".py")
                module = importlib.util.module_from_spec(spec)
                sys.modules["migrations"] = module
                spec.loader.exec_module(module)
                class_name = getattr(module, function_name)
                try:
                    class_name().down()
                    self.update_migrations(migration_file=file_name)
                    print(bcolors.OKGREEN + "Rolled back " + file_name + bcolors.ENDC)
                except Exception as e:
                    print(bcolors.FAIL + "rollback " + file_name + " failed " + bcolors.ENDC)
                    print(e)
                    exit()

        # print(test_migration_02_02_22_2329392.CreateTestMigration().up())

    def update_migrations(self, migration_file):
        connection = DB.get_cursor()
        query = "DELETE FROM migrations WHERE migration = '{}'".format(migration_file)

        connection.execute(query)
        db = DB.get_db()
        db.commit()
        connection.close()
