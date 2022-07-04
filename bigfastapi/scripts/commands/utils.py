from os import listdir
from os.path import isfile, join

from bigfastapi.core.DB import DB


def create_migrations_table():
    connection = DB.get_cursor()
    query = "CREATE TABLE IF NOT EXISTS `migrations` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `migration` VARCHAR(255) NOT NULL , `batch` INT NOT NULL) "
    connection.execute(query)
    connection.close()


def get_db_migrations() -> list:
    connection = DB.get_cursor()
    query = "SELECT * FROM migrations"
    connection.execute(query)
    migrations = list(connection)
    connection.close()
    return migrations


def get_max_batch_number():
    connection = DB.get_cursor()
    query = "SELECT max(batch) FROM migrations"
    connection.execute(query)
    result = list(connection)[0][0]
    connection.close()
    return result


def get_migration_files(migrations_folder):
    migration_files = [f for f in listdir(migrations_folder) if isfile(join(migrations_folder, f))]
    migration_files = [x for x in migration_files if x[0] != '.']
    migration_files = [x for x in migration_files if x[0] != '__']
    migration_files = [x for x in migration_files if x != '__init__.py']
    migration_files.sort()
    return migration_files
