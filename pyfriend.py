#!/usr/bin/python3

import argparse
from PyFriendClass import PyFriendClass

def pyFriendMenuArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                        description="""Clone official python3 docs to your machine with a specific version (example: docs for 3.10.2 or 3.9.1). 
PyFriend can list all python3 standard libraries into your terminal.
PyFriend can display manual of a standard python3 module into your terminal.
PyFriend can open local python3 docs into your browser as html for faster reading, research and coding.

Credits:
    https://elprofesor.io
    https://github.com/elprofesor96/py.friend""")
    parser.add_argument('-l', '--list', help='list all stadard modules', action='store_true')
    parser.add_argument('-m', '--man', help='manual of a module specified by nameOfModule. Ex: pyfriend -m [nameOfModule]', action='store_true')
    parser.add_argument('-d', '--docs', help='open local python3 official docs in a browser', action='store_true')
    parser.add_argument('-r', '--reset', help='reset the database/download a specific version of python3 docs. Ex: pyfriend -r [python3Version]', action='store_true')
    parser.add_argument('nameOfModule', help='nameOfModule is used only with --man command. Example: pyfriend -m os', nargs='*')
    parser.add_argument('python3Version', help='python3Version is used only with --reset command. Example: pyfriend -r 3.11.0', nargs='*')
    args = parser.parse_args()

    pyfriend = PyFriendClass()

    if args.list:
        pyfriend.printAllStandardLibraries()
    elif args.man and args.nameOfModule:
        pyfriend.printHelpOfAModule(args.nameOfModule[0])
    elif args.docs:
        pyfriend.openOfficialDocsFromDb()
    elif args.reset and args.nameOfModule:
        pyfriend.resetDatabase(args.nameOfModule[0])
    else:
        parser.print_help()
          


if __name__ == '__main__':
    pyFriendMenuArguments()
