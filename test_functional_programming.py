

from functional_programming import get_fizzbuzz


def test_get_fizzbuzz():

    # when i == 3, should output 'Fizz'
    assert get_fizzbuzz(3) == 'Fizz'

    # when i == 5, should output 'Buzz'
    assert get_fizzbuzz(5) == 'Buzz'

    # when i == 15, should output 'FizzBuzz'
    assert get_fizzbuzz(15) == 'FizzBuzz'

    # when i == 2, shouldn't output anything
    assert get_fizzbuzz(2) is None