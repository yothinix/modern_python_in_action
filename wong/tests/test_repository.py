from datetime import date
from ward import test

from ..repository import BookRepository


repository = BookRepository()


@test('test find by name should return list of book')
def _():
    actual = repository.find_by_name('Distilled')

    assert 1 == len(actual)
    assert "Python Distilled (Developer's Library)" == actual[0]['name']


@test('test find by name should return empty list when result not match')
def _():
    actual = repository.find_by_name('NOT EXIST')

    assert 0 == len(actual)


@test('test find by author should return list of book')
def _():
    actual = repository.find_by_author('Al Sweigart')

    assert 3 == len(actual)


@test('test get all book order by length should return books')
def _():
    expected = "Fluent Python: Clear, Concise, and Effective Programming " \
        "1st Edition"
    expected2 = 'How to Design Programs: An Introduction to Programming ' \
        'and Computing (The MIT Press) second edition'

    actual = repository.get_all_book(sorted_key='length', reverse=True)

    assert expected == actual[0]['name']
    assert expected2 == actual[1]['name']


@test('test get all book without arguments should return books')
def _():
    expected = 'Automate the Boring Stuff with Python, 2nd Edition: ' \
        'Practical Programming for Total Beginners'

    actual = repository.get_all_book()

    assert expected == actual[0]['name']


@test('test find by date range should return books')
def _():
    expected1 = 'Python Basics: A Practical Introduction to Python 3'
    expected2 = 'Black Hat Python, 2nd Edition: Python Programming for ' \
        'Hackers and Pentesters'
    expected3 = 'Python Programming for Beginners'
    expected4 = 'CPython Internals: Your Guide to the Python 3 Interpreter'

    start = date(2020, 1, 1)
    end = date(2021, 5, 30)

    actual = repository.find_by_date_range(start, end)

    assert 4 == len(actual)
    assert expected1 == actual[0]['name']
    assert expected2 == actual[1]['name']
    assert expected3 == actual[2]['name']
    assert expected4 == actual[3]['name']
