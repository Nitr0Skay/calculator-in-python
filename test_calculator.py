import pytest
from calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 3) == 7

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_modulo():
    calc = Calculator()
    assert calc.modulo(10, 3) == 1

def test_exp():
    calc = Calculator()
    assert calc.exp(2, 3) == 8

def test_divide_by_zero():
    calc = Calculator()

    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)