from datetime import date

from ward import test

from reader import format_date, load_db


@test('test_format_date_should_return_date')
def _() -> None:
    expected = date(2021, 5, 30)
    actual = format_date('May 30, 2021')
    assert expected == actual


@test('test load db should return book list')
def _b() -> None:
    expected = 20
    actual = load_db()
    assert expected == len(actual)
