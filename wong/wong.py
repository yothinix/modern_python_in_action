from pick import pick
from rich.prompt import Prompt

from .repository import BookRepository
from .render import render


def main() -> None:
    repository = BookRepository()

    title = 'Please choose query mode: '
    options = ['List all', 'find by name', 'find by author', 'find by date range']
    _, index = pick(options, title)
    print(index)

    if index == 0:
        is_sort = Prompt.ask("Want to sort?", choices=["Yes", "No"], default="No")
        if is_sort == "Yes":
            sort_choices = ['name', 'author', 'length', 'publisher']
            sort_key = Prompt.ask("Which key we want to sort?", choices=sort_choices, default="name")
            reverse = Prompt.ask("Reverse?", choices=["Yes", "No"], default="No")
            result = repository.get_all_book(sorted_key=sort_key, reverse=reverse == "Yes")
        else:
            result = repository.get_all_book()
    elif index == 1:
        name = Prompt.ask("Which name?: ")
        result = repository.find_by_name(name)
    elif index == 2:
        author = Prompt.ask("Which author?: ")
        result = repository.find_by_author(author)
    elif index == 3:
        pass
    else:
        print('Not choosing any mode end program')

    render(result)
