# Usage

## Temperature conversion

The conversion helpers are defined in `src/calculator.py`:

```python
from src.calculator import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(0))   # 32.0
print(fahrenheit_to_celsius(32))   # 0.0
```

The formulas are:

- Celsius to Fahrenheit: `celsius * 9 / 5 + 32`
- Fahrenheit to Celsius: `(fahrenheit - 32) * 5 / 9`

## Run tests

From the repository root, run:

```bash
python -m pytest
```
