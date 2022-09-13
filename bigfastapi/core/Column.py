class Column:

    def __init__(self, name: str, attributes: list = [], is_change: bool = False, is_update: bool = False,
                 is_delete: bool = False,
                 is_rename: bool = False, is_foreign: bool = False, new_name: str = ''):
        self.name = name
        if not is_foreign:
            attributes.append('NOT NULL')
        self.attributes = attributes
        self.is_rename = is_rename
        self.is_delete = is_delete
        self.is_update = is_update
        self.is_change = is_change
        self.new_name = new_name
        self.is_foreign = is_foreign
        self.reference_column = ''

    def nullable(self):
        if 'NOT NULL' in self.attributes:
            self.attributes.remove('NOT NULL')

        self.attributes.append('NULL')
        return self

    def after(self, name: str):
        self.attributes.append('AFTER')
        self.attributes.append("`" + name + "`")

    def first(self):
        self.attributes.append('FIRST')
        return self

    def unsigned(self):
        if 'SIGNED' in self.attributes:
            self.attributes.remove('SIGNED')
        self.attributes.insert(len(self.attributes) - 1, "UNSIGNED")
        return self

    def primary(self):
        self.attributes.append('PRIMARY KEY')
        return self

    def unique(self):
        self.attributes.append("UNIQUE")

    def auto_increment(self):
        self.attributes.append('AUTO INCREMENT')
        return self

    def references(self, column_name: str):
        self.reference_column = column_name
        return self

    def on(self, table_name: str):
        self.attributes.append('REFERENCES `' + table_name + '`(`' + self.reference_column + '`)')
        return self

    def onDelete(self, option: str):
        self.attributes.append('ON DELETE ' + option)
        return self

    def onUpdate(self, option: str):
        self.attributes.append('ON UPDATE ' + option)
        return self

    def default(self, value: str):
        # todo: Add value to end of array or before last item in list
        self.attributes.append('DEFAULT')
        if value.isnumeric():
            self.attributes.append(value)
        else:
            self.attributes.append("`" + value + "`")
        return self

    def drop(self):
        self.is_delete = True

    def to_string(self) -> str:
        seen = set()
        attributes = [x for x in self.attributes if not (x in seen or seen.add(x))]
        self.attributes = list(attributes)  # remove duplicates
        if self.is_delete:
            return ' DROP COLUMN `' + self.name + '`'
        elif self.is_update:
            if self.is_foreign:
                return ' ADD ' + (' '.join(self.attributes))
            else:
                return ' ADD `' + self.name + '` ' + (' '.join(self.attributes))
        elif self.is_change:
            return ' CHANGE `' + self.name + '` `' + self.new_name + '`' + (' '.join(self.attributes))
        elif self.is_rename:
            return ' RENAME COLUMN `' + self.name + '` TO `' + self.new_name + '`'
        elif self.is_foreign:
            return (' '.join(self.attributes))
        else:
            column = '`' + self.name + '` '
            column += (' '.join(self.attributes))

            return column
