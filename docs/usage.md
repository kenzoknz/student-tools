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
