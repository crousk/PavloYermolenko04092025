import uuid


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.book_id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.title} — {self.author} ({self.book_id})"


class Library:
    def __init__(self, name: str, books: list[Book] = None):
        self.name = name
        self.books = books if books else []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Книга '{book.title}' була додана до бібліотеки '{self.name}'.")

    def remove_book(self, book_id: str):
        for book in self.books:
            if book_id == book_id:
                self.books.remove(book)
                print(f"Книгу '{book.title}' було видалено з бібліотеки '{self.name}'.")
                return
        print(f"Книгу з ID '{book_id}' не знайдено у бібліотеці '{self.name}'.")

    def show_books(self):
        if not self.books:
            print(f"У бібліотеці '{self.name}' немає книг.")
        else:
            print(f"Книги у бібліотеці '{self.name}':")
            for book in self.books:
                print(f"  {book}")

book2 = Book("Harry Potter and the Goblet of Fire", "J. K. Rowling")
book1 = Book("Book for removing", "me")
book3 = Book("1984", "George Orwell")

library = Library("Бібліотека книг")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.remove_book(book3.book_id)

library.show_books()

