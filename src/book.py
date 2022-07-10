class Book:

#!!!!!!menu item
#author of the book, name of the book, note for the book
    def __init__(self, author, name, note):
        self.author = author
        self.name = name
        self.note = note

# test
# book01 = Book("New_Author", "New_Book", "Note")
# print(book01.author)

    #see what is in the library
    def _show_book(self):
        #!!!!!show_item
        print(f"{self.author}, {self.name}")

    #see what is in the library
    def _show_book_notes(self):
        #!!!!!show_item
        print(f"{self.author}, {self.name}, {self.note}")

# test
# book01 = Book("New_Author", "New_Book", "Note")
# book01._show_book()




    
#     def _read_note(self):
#         print(f"{self.author}, {self.name}, {self.note}")
