from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title):
        needed_book = next(b for b in self.books if b.title == title)
        try:
            return f'{needed_book.title} by {needed_book.author}'
        except None:
            return 'The book is not available!'


book0 = Book('Chronic', 'Gosho')
book1 = Book('Something', 'Toni')
library = Library()
library.add_book(book0)
library.add_book(book1)
print(library.find_book('Chronic'))


