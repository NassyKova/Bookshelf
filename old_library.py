from os import system


old_library = [
    ["Jack London", "The Iron Heel", "Political novel"],
    ["Haruki Murakami", "1Q84", "Travels through the time, the girl who kills"],
    ["Strugatsky Brothers", "Hard to Be a God", "Another planet, trying to fix the humanuty"],
    ["Sally Rooney", "Conversations with Friends", "Letter excache between two friends, one is a published author, another lives anordinary life, include other people, plus a third friend, politic and God believer"]
    ]

old_library("1", "2", "3")
print(old_library)
# #list of options
# def _print_options():
#     print("1. Open the library")
#     print("2. Add book to the library")
#     print("3. Add note to the book")
#     print("7. Close the library, exit the bookshelf")
#     opt = input("Select your option (1-7): ")
#     return opt

# # print(_print_options())

def _add_book(catalogue_input, author_name, book_name, note):
    catalogue_input[author_name].append(book_name, note)
    return catalogue_input

_add_book(old_library, "New_Author", "New_Book_Name", "New_Note")
print (old_library)

# def _add_note(catalogue_input, author_name, book_name, note):
#     if author_name not in catalogue_input:
#         catalogue_input[author_name] = [book_name]
#     else:
#         catalogue_input[author_name].append(book_name)
#         catalogue_input[author_name].append(note)
#     return catalogue_input

# option = ""

# while option != "6":
#     system('clear')
#     option = _print_options()
#     system('clear')
#     if option == "1":
#         print(*old_library, sep="\n")
#     elif option == "2":
#         add_product()
#     elif option == "3":
#         edit_product()
#     elif option == "4":
#         delete_product()
#     elif option == "5":
#         take_order()
#     elif option == "6":
#         continue
#     else:
#         print("Invalid option")
        
#     input("press Enter to continue...")
#     system('clear')

# print("Goodbye!") 