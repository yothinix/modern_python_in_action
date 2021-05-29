from .repository import BookRepository
from .render import render


def main() -> None:
    repository = BookRepository()
    result = repository.get_all_book()

    render(result)
