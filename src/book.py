class Book:

#author of the book, name of the book, note for the book
    def __init__(self, author, name, note):
        self.author = author
        self.name = name
        self.note = note

    #see what is in the library
    def show_book(self):
        print(f"{self.author}, {self.name}")

    #see what is in the library
    def show_book_notes(self):
        print(f"{self.author}, {self.name}, {self.note}")

