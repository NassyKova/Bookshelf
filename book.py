class Book:

    def __init__(self, author, name, note):
        self.author = author
        self.name = name
        self.note = note

    def _open_library(self):
        print(f"{self.author}, {self.name}")
    
    def _read_note(self):
        print(f"{self.author}, {self.name}, {self.note}")