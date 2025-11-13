class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability = True

    def display_info(self):
        status = "Available" if self.availability else "Borrowed"
        print(f"{self.title} by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book.title}' removed from the library.")
        else:
            print("Book not found in the library.")

    def borrow_book(self, book):
        if book in self.books and book.availability:
            book.availability = False
            print(f"Book '{book.title}' borrowed.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, book):
        if book in self.books:
            book.availability = True
            print(f"Book '{book.title}' returned.")
        else:
            print("Book not found in the library.")


library = Library()
book1 = Book("oop", "Aravind")
book2 = Book("class", "Aravind")

library.add_book(book1)
library.add_book(book2)
library.borrow_book(book1)
library.return_book(book1)
book1.display_info()
