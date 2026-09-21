# Converter Usage

The `src/converter.py` module provides temperature conversion helpers for `student-tools`.

## Supported Conversion Units

| Unit       | Symbol | Direction            |
| ---------- | ------ | -------------------- |
| Celsius    | °C     | to / from Fahrenheit |
| Fahrenheit | °F     | to / from Celsius    |

> No other temperature units are supported in this version.

## Functions

### `celsius_to_fahrenheit(celsius)`

Converts a temperature from Celsius to Fahrenheit.

| Item         | Description                       |
| ------------ | --------------------------------- |
| Parameter    | `celsius`                         |
| Data type    | `float` or `int`                  |
| Return type  | `float`                           |
| Return value | Temperature in degrees Fahrenheit |

**Formula:**

```text
Fahrenheit = Celsius × 9 / 5 + 32
```

**Example:**

```python
from src.converter import celsius_to_fahrenheit

print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
```

### `fahrenheit_to_celsius(fahrenheit)`

Converts a temperature from Fahrenheit to Celsius.

| Item         | Description                    |
| ------------ | ------------------------------ |
| Parameter    | `fahrenheit`                   |
| Data type    | `float` or `int`               |
| Return type  | `float`                        |
| Return value | Temperature in degrees Celsius |

**Formula:**

```text
Celsius = (Fahrenheit - 32) × 5 / 9
```

**Example:**

```python
from src.converter import fahrenheit_to_celsius

print(fahrenheit_to_celsius(32))   # 0.0
print(fahrenheit_to_celsius(212))  # 100.0
```

## Usage

Temperature conversion helpers can be imported directly from `src.converter`:

```python
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))   # 32.0
print(fahrenheit_to_celsius(32))   # 0.0
```

## Run Tests

From the repository root, run:

```bash
python -m pytest
```

All supported conversion functions should be covered by the project's test suite.
