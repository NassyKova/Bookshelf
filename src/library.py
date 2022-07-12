from book import Book
from intro import _intro, bcolors


class Library:
    # a list of exhisting books
    def __init__(self, books):
        self.books = books

    def _print_library(self):
        _intro()
        print(bcolors.OKBLUE + "     Nice to see you again!\n     These books you've read so far: \n" + bcolors.ENDC)
        for item in self.books:
            item._show_book()

    def _print_library_notes(self):
        _intro()
        print(bcolors.OKBLUE + "     Here a notes for the book you've read: \n" + bcolors.ENDC)
        for item in self.books:
            item._show_book_notes()


    # add a new book to the library
    def _add_item(self, author, name, note):
        new_book = Book(author, name, note)
        self.books.append(new_book)

#delete the book from the library
    def _delete_item(self, name):
        for item in self.books:
            if item.name == name:
                self.books.remove(item)
                return print(bcolors.OKBLUE + f"     I've removed {name} from your library \n" + bcolors.ENDC)
                
        return print(bcolors.OKBLUE + f"     Hm, I couldn't find {name} in your library...\n" + bcolors.ENDC)

# add/edit note to the book
    def _edit_item_note(self, name):
        for item in self.books:
            if item.name == name:
                note = input (bcolors.OKBLUE + f"     What is the new description of {name}?: " + bcolors.ENDC)
                item.note = note
                return print(bcolors.OKBLUE + f"     I've updated the description of {name} \n" + bcolors.ENDC)
        return print(bcolors.OKBLUE + f"     Hm, I couldn't find {name} in your library...\n" + bcolors.ENDC)

