# from ...migrations import *
import importlib.util
import sys
from os import listdir
from os.path import isfile, join

from bigfastapi.core.Command import Command
from bigfastapi.core.DB import DB
# from migrations import test_migration_02_02_22_2329392
# from migrations.test_migration_02_02_22_2329392 import CreateTestMigration
# import migrations._2_create_jobs_table_2022_3_11_23470
from ..print_colors import bcolors


class MigrateRollBackHelper(Command):

    def run(self, args: list = None):
        try:
            self.create_migrations_table()
        except Exception:
            pass

        db_migration_files = self.get_db_migrations()
        # print("to migrate is ", files_to_migrate)
        batch_number = self.get_max_batch_number()
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
                spec = importlib.util.spec_from_file_location("migrations", "migrations/" + migration_file + ".py")
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

    def get_migration_files(self):
        mypath = 'migrations/'
        migration_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        migration_files = [x for x in migration_files if x[0] != '.']
        migration_files = [x for x in migration_files if x[0] != '__']
        migration_files = [x for x in migration_files if x != '__init__.py']
        migration_files.sort()
        return migration_files

    def create_migrations_table(self):
        connection = DB.get_cursor()
        query = "CREATE TABLE IF NOT EXISTS `migrations` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `migration` VARCHAR(255) NOT NULL , `batch` INT NOT NULL) "
        connection.execute(query)
        connection.close()

    def get_db_migrations(self) -> list:
        connection = DB.get_cursor()
        query = "SELECT * FROM migrations"
        connection.execute(query)
        migrations = list(connection)
        connection.close()
        return migrations

    def get_max_batch_number(self):
        connection = DB.get_cursor()
        query = "SELECT max(batch) FROM migrations"
        connection.execute(query)
        result = list(connection)[0][0]
        connection.close()
        return result

    def update_migrations(self, migration_file):
        connection = DB.get_cursor()
        query = "DELETE FROM migrations WHERE migration = '{}'".format(migration_file)

        connection.execute(query)
        db = DB.get_db()
        db.commit()
        connection.close()
