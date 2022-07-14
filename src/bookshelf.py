from os import system
from book import Book
from library import Library
from seed import seed
from intro import intro, bcolors


library = seed()
#bookshelf - cafe

#list of options
def print_options():
    intro()
    print(bcolors.OKBLUE + "     1. Open the library" + bcolors.ENDC)
    print(bcolors.OKBLUE + "     2. Open the library with notes" + bcolors.ENDC)
    print(bcolors.OKBLUE + "     3. Add a book to the library" + bcolors.ENDC)
    print(bcolors.OKBLUE + "     4. Delete the book" + bcolors.ENDC)
    print(bcolors.OKBLUE + "     5. Add/edite note for a book" + bcolors.ENDC)
    print(bcolors.OKBLUE + "     6. Close the library, exit the bookshelf" + bcolors.ENDC)
    opt = input(bcolors.OKBLUE + "     Choose what do you want to do (1-6): " + bcolors.ENDC)
    return opt


# adding a book to the library using method add_item
def add_book():
    intro()
    author = input(bcolors.OKBLUE + "     Who is the author?: " + bcolors.ENDC)
    if author == "":
        return print(bcolors.OKBLUE + f"     You better type something next time\n" + bcolors.ENDC)
    name = input(bcolors.OKBLUE + f"     Which book of {author} you want to add?: " + bcolors.ENDC)
    if name == "":
        return print(bcolors.OKBLUE + f"     You better type something next time\n" + bcolors.ENDC)
    note = input(bcolors.OKBLUE + f"     What was {name} about?: " + bcolors.ENDC)
    library.add_item(author, name, note)
    print(bcolors.OKBLUE + f"\n     I've added {name} to your library" + bcolors.ENDC)

#deleting a book from the library using methid delete_item
def delete_book():
    intro()
    for item in library.books:
        print(item.name)

    name = input(bcolors.OKBLUE + "\n\n     Which book you want to delete?: \n\n"+ bcolors.ENDC)
    # if input is None:
    if name == "":
        return print(bcolors.OKBLUE + f"     You better type something next time\n" + bcolors.ENDC)

    library.delete_item(name)

# edit a book and the elements using method edit_item
def edit_note():
    intro()
    for item in library.books:
        print(item.name)

    name = input(bcolors.OKBLUE + "\n\n     You want to add or edit a note to wich book?: \n\n"+ bcolors.ENDC)
    if name == "":
        return print(bcolors.OKBLUE + f"     You better type something next time\n" + bcolors.ENDC)
    library.edit_item_note(name)


#start options
option = ""

while option != "6":
    system('clear')
    option = print_options()
    system('clear')
    if option == "1":
        library.print_library()
    elif option == "2":
        library.print_library_notes()
    elif option == "3":
        add_book()
    elif option == "4":
        delete_book()
    elif option == "5":
        edit_note()
    elif option == "6":
        continue
    else:
        intro()
        print(bcolors.FAIL +"     \n\nNo such option, try again\n\n" + bcolors.ENDC)
        
    input(bcolors.WARNING + "     \n\npress Enter to continue...\n\n" + bcolors.ENDC)
    system('clear')

intro()
print(bcolors.OKBLUE + "     \n\nGoodbye!\n\n" + bcolors.ENDC) 

