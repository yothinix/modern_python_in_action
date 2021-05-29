from ward import test

from ..repository import BookRepository


@test('test find by name should return list of book')
def _():
    repository = BookRepository()

    actual = repository.find_by_name('Distilled')

    assert 1 == len(actual)
    assert "Python Distilled (Developer's Library)" == actual[0]['name']


@test('test find by name should return empty list when result not match')
def _():
    repository = BookRepository()

    actual = repository.find_by_name('NOT EXIST')

    assert 0 == len(actual)
