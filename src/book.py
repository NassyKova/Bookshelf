class Book:

#author of the book, name of the book, note for the book
    def __init__(self, author, name, note):
        self.author = author
        self.name = name
        self.note = note

    #see what is in the library
    def _show_book(self):
        #!!!!!show_item
        print(f"{self.author}, {self.name}")

    #see what is in the library
    def _show_book_notes(self):
        #!!!!!show_item
        print(f"{self.author}, {self.name}, {self.note}")

