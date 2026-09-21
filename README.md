# student-tools

Small utilities for learning and practicing open-source development workflows.

## Temperature conversion

The project includes helpers for converting between Celsius and Fahrenheit:

```python
from src.calculator import celsius_to_fahrenheit, fahrenheit_to_celsius

fahrenheit = celsius_to_fahrenheit(25)  # 77.0
celsius = fahrenheit_to_celsius(77)      # 25.0
```

See [docs/usage.md](docs/usage.md) for setup and usage details.

Temperature inputs can be checked with `validate_temperature` before conversion.
