from book import Book
from intro import intro, bcolors
from error import no_such_book, type_something


class Library:
    # a list of exhisting books
    def __init__(self, books):
        self.books = books

    def print_library(self):
        intro()
        print(bcolors.OKBLUE + "\n     These books you've read so far: \n" + bcolors.ENDC)
        for item in self.books:
            item.show_book()

    def print_library_notes(self):
        intro()
        print(bcolors.OKBLUE + "     Here a notes for the book you've read: \n" + bcolors.ENDC)
        for item in self.books:
            item.show_book_notes()


    # add a new book to the library
    def add_item(self, author, name, note):
        new_book = Book(author, name, note)
        self.books.append(new_book)

#delete the book from the library
    def delete_item(self, name):
        for item in self.books:
            if item.name == name:
                self.books.remove(item)
                return print(bcolors.OKBLUE + f"     I've removed {name} from your library \n" + bcolors.ENDC)
        no_such_book()

# add/edit note to the book
    def edit_item_note(self, name):
        for item in self.books:
            if item.name == name:
                note = input (bcolors.OKBLUE + f"     What is the new description of {name}?: " + bcolors.ENDC)
                if note == "":
                    type_something()
                item.note = note
                return print(bcolors.OKBLUE + f"     I've updated the description of {name} \n" + bcolors.ENDC)
        no_such_book()

