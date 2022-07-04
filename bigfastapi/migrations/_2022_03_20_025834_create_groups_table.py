from bigfastapi.core.Blueprint import Blueprint as Blueprint
from bigfastapi.core.Schema import Schema


class CreateGroupsTable:

    def schema(self, table: Blueprint):
        table.id()
        table.string('name')
        table.boolean('send_email_alert')
        table.boolean('send_sms_alert')
        table.timestamps()

    def up(self):
        Schema.create(table_name="groups", schema=self.schema)

    def down(self):
        Schema.dropIfExist(table_name="groups")
