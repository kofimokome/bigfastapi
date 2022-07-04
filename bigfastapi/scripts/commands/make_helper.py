import argparse

from bigfastapi.core.Command import Command
from ..print_colors import bcolors


class MakeHelper(Command):

    def run(self, args: list = None):
        parser = argparse.ArgumentParser(description="Create a new helper command")
        parser.add_argument('helper_name', help='Name of migration file',
                            type=str)
        args = parser.parse_args(args)

        file_name = args.helper_name.strip()
        snake_str = file_name.lower()
        file_name = snake_str + ".py"
        components = snake_str.split('_')
        class_name = components[0].title() + ''.join(x.title() for x in components[1:]) + 'Helper'

        contents = '''from bigfastapi.core.Command import Command


class ''' + class_name + '''(Command):

    def run(self, args: list = None):
        print("args are ", args)
'''
        file = open('bigfastapi/scripts/commands/' + file_name, 'a')
        file.write(contents)
        print(bcolors.OKGREEN + "Helper created at helpers/commands/" + file_name + ' created')
