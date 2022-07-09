class Book:
#author of the book, name of the book, note for the book
    def __init__(self, author, name):
        self.author = author
        self.name = name
        self.note = note

    #see what is in the library
    def _open_library(self):
        print(f"{self.author}, {self.name}")
    
    def _read_note(self):
        print(f"{self.author}, {self.name}, {self.note}")




