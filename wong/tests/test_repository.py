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


@test('test get all book order by length should return a book')
def _():
    expected = "Fluent Python: Clear, Concise, and Effective Programming " \
        "1st Edition"
    expected2 = 'How to Design Programs: An Introduction to Programming ' \
        'and Computing (The MIT Press) second edition'

    actual = repository.get_all_book(sorted_key='length', reverse=True)

    assert expected == actual[0]['name']
    assert expected2 == actual[1]['name']
