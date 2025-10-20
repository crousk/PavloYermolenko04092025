import pytest
from project.hw_15_class.library import Book, Library

@pytest.fixture
def sample_books():
    return [
        Book("The Hobbit", "J. R. R. Tolkien"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("1984", "George Orwell"),
    ]

@pytest.fixture
def empty_library():
    return Library("Тестова бібліотека")

class TestLibrary:
    @pytest.mark.parametrize("book_index", [0, 1, 2])
    def test_add_book(self, empty_library, sample_books, book_index):
        book = sample_books[book_index]
        empty_library.add_book(book)
        assert book in empty_library.books
        assert len(empty_library.books) == 1

    @pytest.mark.parametrize("remove_index", [0, 1, 2])
    def test_remove_book(self, empty_library, sample_books, remove_index, capsys):
        for book in sample_books:
            empty_library.add_book(book)

        book_to_remove = sample_books[remove_index]
        empty_library.remove_book(book_to_remove.book_id)
        captured = capsys.readouterr()

        assert book_to_remove not in empty_library.books
        assert f"Було видалено з бібліотеки" in captured.out

    @pytest.mark.parametrize("book_count", [0, 1, 3])
    def test_show_books(self, empty_library, sample_books, book_count, capsys):
        for i in range(book_count):
            empty_library.add_book(sample_books[i])

        empty_library.show_books()
        output = capsys.readouterr().out

        if book_count == 0:
            assert "Немає книг" in output
        else:
            assert "Книги у бібліотеці" in output
            assert str(sample_books[0].title) in output or str(sample_books[-1].title) in output