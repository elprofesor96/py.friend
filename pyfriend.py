import argparse
from PyFriendClass import PyFriendClass

def credit():
    rulerzCredit =  """ 
                _                ___   __   
     _ __ _   _| | ___ _ __ ____/ _ \ / /_  
    | '__| | | | |/ _ \ '__|_  / (_) | '_ \ 
    | |  | |_| | |  __/ |   / / \__, | (_) |
    |_|   \__,_|_|\___|_|  /___|  /_/ \___/ 
        """
    return rulerzCredit

def pyFriendMenuArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                        description=credit())
    parser.add_argument('-l', '--list', help='list all stadard modules', action='store_true')
    parser.add_argument('-m', '--man', help='manual of a module specified by nameOfModule', action='store_true')
    parser.add_argument('-d', '--docs', help='open search box in official docs [html form]', action='store_true')
    parser.add_argument('-r', '--reset', help='reset the database. [download new one from official site]', action='store_true')
    parser.add_argument('nameOfModule', help='nameOfModule is used only with --man command', nargs='*')
    args = parser.parse_args()

    pyfriend = PyFriendClass()

    if args.list:
            pyfriend.printAllStandardLibraries()
    if args.man:
            pyfriend.printHelpOfAModule(args.nameOfModule[0])
    if args.docs:
            pyfriend.openOfficialDocsFromDb()
    if args.reset:
            pyfriend.resetDatabase()

if __name__ == '__main__':
    pyFriendMenuArguments()