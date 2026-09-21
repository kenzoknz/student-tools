def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def _validate_number(value):
    """Raise TypeError if value is not an int or float."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Input must be a number, got {type(value).__name__}")


def add(a, b):
    _validate_number(a)
    _validate_number(b)
    return a + b


def subtract(a, b):
    _validate_number(a)
    _validate_number(b)
    return a - b


def multiply(a, b):
    _validate_number(a)
    _validate_number(b)
    return a * b


def divide(a, b):
    _validate_number(a)
    _validate_number(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b