from datetime import date

from ward import test

from ..reader import format_date


@test('test_format_date_should_return_date')
def _():
    expected = date(2021, 5, 30)
    actual = format_date('May 30, 2021')
    assert expected == actual
