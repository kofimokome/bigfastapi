# from ...migrations import *
import os
import shutil
import sys
from os.path import join

from dotenv import load_dotenv

from bigfastapi.core.Command import Command
from .utils import get_migration_files
from ..print_colors import bcolors

load_dotenv('.env')
MIGRATIONS_FOLDER = os.environ.get("MIGRATIONS_FOLDER")


class MigrateSyncHelper(Command):

    def run(self, args: list = None):
        path = 'migrations/'
        pkgdir = sys.modules['bigfastapi'].__path__[0]
        migrations_path = os.path.join(pkgdir, path)

        migration_files = get_migration_files(migrations_path)
        migration_files = [join(migrations_path, x) for x in migration_files]

        for migration_file in migration_files:
            file_name = migration_file[:-3]
            print(bcolors.WARNING + "Copying " + file_name + bcolors.ENDC)
            try:
                shutil.copy(migration_file, MIGRATIONS_FOLDER)
                print(bcolors.OKGREEN + "Done copying " + file_name + bcolors.ENDC)
            except Exception as e:
                print(bcolors.FAIL + "copying " + file_name + " failed " + bcolors.ENDC)
                print(e)
                exit()
        print(bcolors.OKGREEN + "Sync complete. You can run bigfastapi migrate " + bcolors.ENDC)
