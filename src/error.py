from intro import bcolors
from book import Book


def type_something():
    return print(bcolors.OKBLUE + "     You better type something next time\n" + bcolors.ENDC)

def no_such_book():
    return print(bcolors.OKBLUE + "     Hm, I couldn't find it in your library...\n" + bcolors.ENDC)
