"""Temperature converter utilities for student-tools.

This module converts values between the currently supported temperature
units. Each public function documents its parameters, types, and return
value so callers can integrate the converter without reading the source.

Supported conversion units
--------------------------
- Celsius (°C)
- Fahrenheit (°F)
"""


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula used: F = C * 9 / 5 + 32

    Args:
        celsius (float | int): Temperature in degrees Celsius.

    Returns:
        float: Equivalent temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    # Scale Celsius by 9/5, then shift by the freezing-point offset (32).
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius.

    Formula used: C = (F - 32) * 5 / 9

    Args:
        fahrenheit (float | int): Temperature in degrees Fahrenheit.

    Returns:
        float: Equivalent temperature in degrees Celsius.

    Examples:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    # Remove the Fahrenheit offset, then scale back to the Celsius range.
    return (fahrenheit - 32) * 5 / 9
