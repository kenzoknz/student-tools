# student-tools

Small utilities for learning and practicing open-source development workflows.

## Converter

The converter module provides helpers for converting temperatures between Celsius and Fahrenheit.

Currently supported units:

* Celsius (°C)
* Fahrenheit (°F)

### How to Call the Functions

```python
from src.converter import celsius_to_fahrenheit, fahrenheit_to_celsius

# Celsius → Fahrenheit
# Parameter: celsius (float | int)
# Returns: float (degrees Fahrenheit)
fahrenheit = celsius_to_fahrenheit(25)
print(fahrenheit)  # 77.0

celsius_to_fahrenheit(0)    # 32.0
celsius_to_fahrenheit(100)  # 212.0

# Fahrenheit → Celsius
# Parameter: fahrenheit (float | int)
# Returns: float (degrees Celsius)
celsius = fahrenheit_to_celsius(77)
print(celsius)  # 25.0

fahrenheit_to_celsius(32)   # 0.0
fahrenheit_to_celsius(212)  # 100.0
```

## Temperature Conversion Formulas

* Celsius to Fahrenheit: `celsius * 9 / 5 + 32`
* Fahrenheit to Celsius: `(fahrenheit - 32) * 5 / 9`

## Documentation

See [docs/usage.md](docs/usage.md) for parameter types, return values, formulas, and additional usage notes.

## Run Tests

From the repository root, run:

```bash
python -m pytest
```
