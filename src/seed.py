from book import Book
from library import Library

def seed():
    book01 = Book("Jack London", "The Iron Heel", "Political novel")
    book02 = Book("Haruki Murakami", "1Q84", "Travels through the time, the girl who kills")
    book03 = Book("Strugatsky Brothers", "Hard to Be a God", "Another planet, trying to fix the humanuty")
    book04 = Book("Sally Rooney", "Conversations with Friends", "Letter exchange between two friends, one is a published author, another lived an ordinary life, include other people, plus a third friend, politic and God believer")

    library = Library([book01, book02, book03, book04])
    return library

print(seed())