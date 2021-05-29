from rich.console import Console
from rich.table import Table

from model import Book

from utils import get_random_color


def render_header(table: Table, book: Book) -> Table:
    for key, _ in book.items():
        table.add_column(key, style=get_random_color(), justify='right')
    return table


def render_row(book: Book) -> list[str]:
    row = []
    for key, _ in book.items():
        row.append(str(book.get(key)))
    return row


def render(result: list[Book]) -> None:
    table = Table(title='Kamar-Taj Library')

    table = render_header(table, result[0])

    for row in result:
        table.add_row(*render_row(row), end_section=True)

    console = Console()
    console.print(table)
