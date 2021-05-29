from pick import pick
from rich.prompt import Prompt

from .repository import BookRepository
from .render import render
from .utils import get_date_input


def main() -> None:
    repository = BookRepository()

    title = "Please choose query mode: "
    options = [
        "List all",
        "find by name",
        "find by author",
        "find by date range"]
    option, index = pick(options, title)
    print(f"Current mode: {index}: {option}")

    if index == 0:
        is_sort = Prompt.ask(
            "Want to sort?", choices=["Yes", "No"], default="No")
        if is_sort == "Yes":
            sort_choices = ["name", "author", "length", "publisher"]
            sort_key = Prompt.ask(
                "Which key we want to sort?",
                choices=sort_choices, default="name"
            )
            reverse = Prompt.ask(
                "Reverse?", choices=["Yes", "No"], default="No")
            result = repository.get_all_book(
                sorted_key=sort_key, reverse=reverse == "Yes"
            )
        else:
            result = repository.get_all_book()
    elif index == 1:
        name = Prompt.ask("Which name?: ")
        result = repository.find_by_name(name)
    elif index == 2:
        author = Prompt.ask("Which author?: ")
        result = repository.find_by_author(author)
    elif index == 3:
        raw_start_date = Prompt.ask("Enter start date (YYYY-MM-DD): ")
        raw_end_date = Prompt.ask("Enter start date (YYYY-MM-DD): ")

        result = repository.find_by_date_range(
            start_date=get_date_input(raw_start_date),
            end_date=get_date_input(raw_end_date),
        )
    else:
        print("Not choosing any mode end program")

    render(result)
