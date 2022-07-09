from os import system
from book import Book
from library import Library
from seed import _seed

library = _seed()
#bookshelf - cafe

#list of options
def _print_options():
    print("1. Open the library")
    print("2. Add a book to the library")
    print("3. Add a note to the book")
    print("4. Delethe the book")
    print("5. Close the library, exit the bookshelf")
    opt = input("Select your option (1-5): ")
    return opt


# adding a book to the library
def _add_book():
    author = input("Who is the author?: ")
    name = input(f"Which book of {author} you want to add?: ")
    note = input(f"What was the {name} about?: ")
    library._add_item(author, name, note)
    print(f"I've added {name} to your library")

# def _delete_book():
#     for item in library.books:
#         print(item.name)

#     name = input("Which book you want to ")

option = ""

while option != "6":
    system('clear')
    option = _print_options()
    system('clear')
    if option == "1":
        library._print_library()
    elif option == "2":
        _add_book()
    elif option == "3":
        add_note()
    elif option == "4":
        delete_book()
    else:
        print("Invalid option")
        
    input("press Enter to continue...")
    system('clear')

print("Goodbye!") 

