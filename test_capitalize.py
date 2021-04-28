"""
This is test program to learn pytest module
This will test capitalization function
"""
# test_capitalize.py
# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest

def capital_case(input_value):
    """
    Fucntion to capitalize
    """
    if not isinstance(input_value, str):
        raise TypeError('Please provide a string argument')
    return input_value.capitalize()

def test_capital_case():
    """
    Fucntion to test capitalize
    """
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    """
    Fucntion to test capitalize exception
    """
    with pytest.raises(TypeError):
        capital_case(9)
