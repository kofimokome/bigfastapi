from .Column import Column


class Blueprint:

    def __init__(self, is_update: bool = False):
        self.columns = []
        self.is_update = is_update

    def id(self) -> Column:
        column = Column(name='id', attributes=['BIGINT', 'UNSIGNED', 'AUTO_INCREMENT', 'PRIMARY KEY'],
                        is_update=self.is_update)
        self.columns.append(column)
        return column

    def string(self, name: str, size: int = 255) -> Column:
        column = Column(name=name, attributes=['VARCHAR(' + str(size) + ')'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def text(self, name: str) -> Column:
        column = Column(name=name, attributes=['TEXT'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def integer(self, name: str) -> Column:
        column = Column(name=name, attributes=['INTEGER', 'SIGNED'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def big_int(self, name: str) -> Column:
        column = Column(name=name, attributes=['BIGINT', 'SIGNED'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def boolean(self, name: str) -> Column:
        column = Column(name=name, attributes=['BOOL'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def date_time(self, name: str) -> Column:
        column = Column(name=name, attributes=['DATETIME'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def timestamps(self):
        self.date_time('created_at').nullable()
        self.date_time('updated_at').nullable()

    def soft_delete(self):
        self.boolean('deleted').nullable().default(value=0)

    def date(self, name: str) -> Column:
        column = Column(name=name, attributes=['DATE'], is_update=self.is_update)
        self.columns.append(column)
        return column

    def long_text(self, name: str):
        return ''

    def drop(self, name: str):
        column = Column(name=name, is_delete=True)
        self.columns.append(column)

    # def change(self, name: str, new_name: str) -> Column:
    #     column = Column(name=name, new_name=new_name, is_change=True)
    #     self.columns.append(column)
    #     return column

    def rename(self, name: str, new_name: str):
        column = Column(name=name, new_name=new_name, is_rename=True)
        self.columns.append(column)

    def foreign(self, column_name) -> Column:
        column = Column(name='', attributes=['FOREIGN KEY (`' + column_name + '`)'], is_foreign=True,
                        is_update=self.is_update)
        self.columns.append(column)
        return column

    def to_string(self) -> str:
        query = [x.to_string() for x in self.columns]
        query = ",".join(query)
        return query

    def get_columns(self):
        return self.columns
