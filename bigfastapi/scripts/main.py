import sys

from .helpers import HELPERS
from .print_colors import bcolors



def print_commands():
    print("Available Commands: ")
    for x_helper in HELPERS:
        print(bcolors.OKGREEN + x_helper + bcolors.ENDC + ": " + HELPERS[x_helper][1])


def main(argv=None):
    arguments = sys.argv

    if arguments is not None and len(arguments) > 1:
        helper = arguments[1]
        print("Running: ", helper)
        if helper in HELPERS:
            command = HELPERS[helper][0]
            arguments = arguments[2:]
            command().run(args=arguments)

        else:
            print(bcolors.FAIL + "Helper " + helper + " is not a valid command." + bcolors.ENDC)
            print_commands()
    else:
        print_commands()
