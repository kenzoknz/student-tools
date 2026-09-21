import pytest
from src.calculator import celsius_to_fahrenheit, fahrenheit_to_celsius
from src.calculator import add, subtract, multiply, divide

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

# --- Trường hợp hợp lệ ---
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


# --- Validation: sai kiểu dữ liệu ---
@pytest.mark.parametrize("func", [add, subtract, multiply, divide])
@pytest.mark.parametrize("bad_value", ["2", None, [1], True])
def test_invalid_type_raises_type_error(func, bad_value):
    with pytest.raises(TypeError):
        func(bad_value, 1)
    with pytest.raises(TypeError):
        func(1, bad_value)


# --- Validation: chia cho 0 ---
def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)
