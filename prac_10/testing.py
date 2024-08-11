"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    # Capitalize the first letter and add a period if it's not already present.
    sentence = phrase.capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # Testing if Car sets the fuel correctly when a value is passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly when a value is passed in."

    # Testing if Car sets the fuel correctly when the default value is used
    test_car_default = Car()
    assert test_car_default.fuel == 0, "Car does not set fuel correctly when default value is used."


run_tests()

# Uncomment the following line to run the doctests
doctest.testmod()
