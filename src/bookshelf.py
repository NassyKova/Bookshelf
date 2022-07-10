from os import system
from book import Book
from library import Library
from seed import _seed
from intro import _intro
from intro import bcolors

library = _seed()
#bookshelf - cafe

#list of options
def _print_options():
    _intro()
    print(bcolors.OKBLUE + "1. Open the library" + bcolors.ENDC)
    print(bcolors.OKBLUE + "2. Open the library with notes" + bcolors.ENDC)
    print(bcolors.OKBLUE + "3. Add a book to the library" + bcolors.ENDC)
    print(bcolors.OKBLUE + "4. Delete the book" + bcolors.ENDC)
    print(bcolors.OKBLUE + "5. Close the library, exit the bookshelf" + bcolors.ENDC)
    opt = input(bcolors.OKBLUE + "Select your option (1-6): " + bcolors.ENDC)
    return opt


# adding a book to the library
def _add_book():
    _intro()
    author = input(bcolors.OKBLUE + "Who is the author?: " + bcolors.ENDC)
    name = input(bcolors.OKBLUE + f"Which book of {author} you want to add?: " + bcolors.ENDC)
    note = input(bcolors.OKBLUE + f"What was the {name} about?: " + bcolors.ENDC)
    library._add_item(author, name, note)
    print(bcolors.OKBLUE + f"\nI've added {name} to your library" + bcolors.ENDC)

def _delete_book():
    for item in library.books:
        print(item.name)

    name = input(bcolors.OKBLUE + "Which book you want to delete?: "+ bcolors.ENDC)
    library._delete_item(name)



option = ""

while option != "5":
    system('clear')
    option = _print_options()
    system('clear')
    if option == "1":
        library._print_library()
    if option == "2":
        library._print_library_notes()
    elif option == "3":
        _add_book()
    elif option == "4":
        _delete_book()

    else:
        print(bcolors.FAIL +"\n\nInvalid option" + bcolors.ENDC)
        
    input(bcolors.WARNING + "\n\npress Enter to continue..." + bcolors.ENDC)
    system('clear')

print(bcolors.OKBLUE + "\n\nGoodbye!" + bcolors.ENDC) 

