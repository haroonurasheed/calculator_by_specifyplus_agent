import pytest
from src.calculator.logic import calculate

def test_basic_addition():
    assert calculate("2 + 3") == 5.0
    assert calculate("10 + 20") == 30.0

def test_basic_subtraction():
    assert calculate("10 - 5") == 5.0
    assert calculate("5 - 10") == -5.0

def test_basic_multiplication():
    assert calculate("4 * 5") == 20.0
    assert calculate("0 * 10") == 0.0

def test_basic_division():
    assert calculate("10 / 2") == 5.0
    assert calculate("5 / 2") == 2.5

def test_pemdas_chained_operations():
    # Multiplication before addition
    assert calculate("2 + 3 * 4") == 14.0
    # Division before subtraction
    assert calculate("10 - 6 / 2") == 7.0
    # Parentheses first
    assert calculate("(2 + 3) * 4") == 20.0
    # Nested parentheses
    assert calculate("((2 + 3) * 2) + 1") == 11.0

def test_decimal_numbers():
    assert calculate("2.5 + 2.5") == 5.0
    assert calculate("10 / 4") == 2.5

def test_empty_input():
    assert calculate("") == 0.0

def test_single_number():
    assert calculate("42") == 42.0

def test_division_by_zero():
    assert calculate("10 / 0") == "Error"
    assert calculate("5 / (2 - 2)") == "Error"

def test_invalid_syntax():
    assert calculate("2 + + 3") == "Error"
    assert calculate("10 * / 2") == "Error"
    assert calculate("(") == "Error"
    assert calculate("())") == "Error"
    assert calculate("invalid") == "Error"
