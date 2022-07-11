from book import Book
from intro import _intro
from intro import bcolors
#library - menu

class Library:
    # a list of exhisting books
    #books = menu_items
    def __init__(self, books):
        self.books = books

    def _print_library(self):
        _intro()
        print(bcolors.OKBLUE + "Nice to see you again!\nThese books you've read so far: \n" + bcolors.ENDC)
        for item in self.books:
            item._show_book()
        # print(self._seed())

    def _print_library_notes(self):
        _intro()
        print(bcolors.OKBLUE + "Nice to see you again!\nThese books you've read so far: \n" + bcolors.ENDC)
        for item in self.books:
            item._show_book_notes()
        # print(self._seed())


    # add a new book to the library
    def _add_item(self, author, name, note):
        new_book = Book(author, name, note)
        self.books.append(new_book)

#delete the book from the library
    def _delete_item(self, name):
        for item in self.books:
            if item.name == name:
                self.books.remove(item)
                return print(bcolors.OKBLUE + f"I've removed {name} from your library \n" + bcolors.ENDC)
                
        return print(bcolors.OKBLUE + f"Hm, I couldn't find {name} in your library...\n" + bcolors.ENDC)

    def _edit_item_note(self, name):
        for item in self.books:
            if item.name == name:
                note = input (bcolors.OKBLUE + f"What is the new description of {name}?: " + bcolors.ENDC)
                item.note = note
                return print(bcolors.OKBLUE + f"I've updated the description of {name} \n" + bcolors.ENDC)
        return print(bcolors.OKBLUE + f"Hm, I couldn't find {name} in your library...\n" + bcolors.ENDC)




# book01 = Book("New_Author", "New_Book", "Note")
# book02 = Book("New_Author1", "New_Book1", "Not1e")
# book03 = Book("New_Author2", "New_Book2", "Note2")

# library = Library([book01, book02, book03])
# library._print_library()







#     def _add_note(self, name, note):
#         for item in self.books:
#             if item.name == name:
#                 note = (f"What would you like to add as a note for {name}?: ")
#                 if () == None:
#                     print("No notes? Fine by me")
#                 return print(f"A note for {name} was added")
#         return print(f"I could not find {name} in your library")




#_-----------------------------
# class Menu:
#     # a list of menu items
#     def __init__(self, menu_items):
#         self.menu_items = menu_items = !!!books

#     def print_menu(self):
#         print("Welcome to Coder Cafe, this is our menu:")
#         for item in self.menu_items:
#             item.show_item() = !!!open_library
#     # adds a new item to the menu
    
    # def add_item(self, name, price):
    #     #self.menu_items.append(MenuItem(name, price))
    #     new_item = MenuItem(name, price) = !!!Book
    #     self.menu_items.append(new_item)

    # def delete_item(self, name):
    #     # iterate through the list looking for the item
    #     for item in self.menu_items:
    #         # check if the item's name of this iteration is equal to the name we receive.
    #         if item.name == name:
    #             # access to the list and remove the item
    #             self.menu_items.remove(item)
    #             return print(f"{name} was removed from the menu")
    
    #     return  print(f"{name} is not in the menu")   

    # def update_price(self, name):
    #     # iterate through the list looking for the item
    #     for item in self.menu_items:
    #         # check if the item's name of this iteration is equal to the name we receive.
    #         if item.name == name:
    #             # ask for the new price
    #             price = float(input(f"What is the new price for {name}? "))
    #             #update the item's price
    #             item.price = price
    #             return print(f"{name}'s price was uptaded in the menu")
    
    #     return  print(f"{name} is not in the menu")   