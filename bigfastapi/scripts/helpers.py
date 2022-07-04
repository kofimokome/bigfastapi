# add helpers here
from .commands.make_helper import MakeHelper
from .commands.make_migration import MakeMigrationHelper
from .commands.migrate import MigrateHelper
# from .commands.migrate_copy import MigrateCopyHelper
from .commands.migrate_rollback import MigrateRollBackHelper
from .commands.migrate_sync import MigrateSyncHelper

HELPERS = {
    'make:migration': [MakeMigrationHelper, 'Creates a migration file'],
    'make:helper': [MakeHelper, 'Creates a helper command. Only on bigfast'],
    'migrate': [MigrateHelper, 'Migrate tables to the database'],
    'migrate:rollback': [MigrateRollBackHelper, 'Rolls back the last run migration(s)'],
    'migrate:sync': [MigrateSyncHelper, 'Syncs bigfastapi migrations with your migrations folder'],
}

# 'migrate:sync': [MigrateSyncHelper, 'Syncs your database migrations with bigfastapi migrations. This command will not run your migrations'],
# 'migrate:copy': [MigrateCopyHelper, 'Copies bigfastapi migrations into your migration folder']
