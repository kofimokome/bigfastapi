# from ...migrations import *
import importlib.util
import os
import sys
from os import listdir
from os.path import isfile, join

from dotenv import load_dotenv

from bigfastapi.core.Command import Command
from bigfastapi.core.DB import DB
from .utils import create_migrations_table, get_db_migrations, get_migration_files, get_max_batch_number
from ..print_colors import bcolors

load_dotenv('.env')

MIGRATIONS_FOLDER = os.environ.get("MIGRATIONS_FOLDER")


class MigrateHelper(Command):

    def run(self, args: list = None):
        try:
            create_migrations_table()
        except Exception:
            pass

        db_migration_files = get_db_migrations()
        db_migration_files = [x[1] for x in db_migration_files]
        migration_files = get_migration_files(MIGRATIONS_FOLDER)
        files_to_migrate = [x for x in migration_files if x[:-3] not in db_migration_files]
        # print("to migrate is ", files_to_migrate)
        batch_number = get_max_batch_number()
        if batch_number is None:
            batch_number = 0

        batch_number = batch_number + 1
        if len(files_to_migrate) == 0:
            print(bcolors.OKGREEN + "Migration files are up to date " + bcolors.ENDC)
        else:
            for migration_file in files_to_migrate:
                file_name = migration_file[:-3]
                print(bcolors.WARNING + "Migrating " + file_name + bcolors.ENDC)
                function_name = file_name.split('_')
                function_name = [x.title() for x in function_name if not x.isnumeric()]
                function_name = ''.join(function_name)
                # module = importlib.import_module('migrations.' + file_name, function_name)
                spec = importlib.util.spec_from_file_location("migrations", MIGRATIONS_FOLDER + migration_file)
                module = importlib.util.module_from_spec(spec)
                sys.modules["migrations"] = module
                spec.loader.exec_module(module)
                class_name = getattr(module, function_name)

                try:
                    class_name().up()
                    self.update_migrations(batch_number=batch_number, migration_file=file_name)
                    print(bcolors.OKGREEN + "Done migrating " + file_name + bcolors.ENDC)
                except Exception as e:
                    print(bcolors.FAIL + "migrating " + file_name + " failed " + bcolors.ENDC)
                    print(e)
                    exit()

    def update_migrations(self, batch_number, migration_file):
        connection = DB.get_cursor()

        query = "INSERT INTO migrations(migration,batch) VALUES('{}', {})".format(migration_file,
                                                                                  batch_number)
        connection.execute(query)
        db = DB.get_db()
        db.commit()
        connection.close()
