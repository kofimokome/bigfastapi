# add helpers here
from .commands.make_helper import MakeHelper
from .commands.make_migration import MakeMigrationHelper
from .commands.migrate import MigrateHelper
from .commands.migrate_rollback import MigrateRollBackHelper

HELPERS = {
    'make:migration': [MakeMigrationHelper, 'Creates a migration file'],
    'make:helper': [MakeHelper, 'Creates a helper command'],
    'migrate': [MigrateHelper, 'another description here'],
    'migrate:rollback': [MigrateRollBackHelper, 'anothe description here']
}
