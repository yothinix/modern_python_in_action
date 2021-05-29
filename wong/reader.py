import csv
from datetime import datetime, date

from .model import Book


def format_date(raw_date: str) -> date:
    return datetime.strptime(raw_date, '%B %d, %Y').date()


def load_db(filename: str = 'book-db.csv') -> list[Book]:
    books = []
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            books.append({
                'name': row['name'],
                'author': row['author'],
                'length': int(row['length']),
                'language': row['language'],
                'publication_date': format_date(row['publication_date']),
                'isbn13': row['isbn13'],
                'publisher': row['publisher']
            })

    return books