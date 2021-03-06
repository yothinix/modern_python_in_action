from datetime import date
from reader import load_db
from model import Book


class BookRepository:
    books: list[Book]

    def __init__(self, file_name: str = './book-db.csv') -> None:
        self.books = load_db(file_name)

    def find_by_name(self, name: str) -> list[Book]:
        return [book for book in self.books if name in book['name']]

    def find_by_author(self, author: str) -> list[Book]:
        return [book for book in self.books if author in book['author']]

    def get_all_book(
        self, sorted_key: str = 'name', reverse: bool = False
    ) -> list[Book]:

        return sorted(
            self.books,
            key=lambda book: (book[sorted_key]),
            reverse=reverse)

    def find_by_date_range(
        self, start_date: date, end_date: date
    ) -> list[Book]:
        return [
            book
            for book in self.books
            if start_date < book['publication_date'] < end_date]
