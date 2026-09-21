# Usage

## Temperature conversion

The conversion helpers are defined in `src/calculator.py`:

```python
from src.calculator import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))   # 32.0
print(fahrenheit_to_celsius(32))   # 0.0
```

## Validate temperature input

Use `validate_temperature` to check that a value is numeric, finite, uses a
supported unit (`C` or `F`), and is not below absolute zero:

```python
from src.validator import validate_temperature

validate_temperature(25, "C")       # True
validate_temperature(-300, "C")     # False
validate_temperature("25", "C")     # False
```

The formulas are:

- Celsius to Fahrenheit: `celsius * 9 / 5 + 32`
- Fahrenheit to Celsius: `(fahrenheit - 32) * 5 / 9`

## Run tests
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

To measure validator coverage, install the optional `coverage` tool and run:

```bash
python -m pip install coverage
python -m coverage run -m pytest
python -m coverage report -m src/validator.py
```
All supported conversion functions should be covered by the project's test suite.
