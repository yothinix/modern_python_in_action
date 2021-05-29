from wong.reader import load_db
from .model import Book


class BookRepository:
    books: list[Book]

    def __init__(self, file_name='book-db.csv') -> None:
        self.books = load_db(file_name)

    def find_by_name(self, name: str) -> list[Book]:
        return [book for book in self.books if name in book['name']]
