from datetime import date
from random import choice


def get_random_color() -> str:
    return choice([
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white'])


def get_date_input(raw_date: str) -> date:
    year, month, day = map(int, raw_date.split('-'))
    return date(year, month, day)
