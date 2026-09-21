import math

import pytest

from src.validator import validate_temperature


@pytest.mark.parametrize(
	("value", "unit"),
	[
		(0, "C"),
		(25.5, "c"),
		(-273.15, "C"),
		(32, "F"),
		(-459.67, "f"),
		(100, "  C  "),
	],
)
def test_validate_temperature_accepts_valid_values(value, unit):
	assert validate_temperature(value, unit) is True


@pytest.mark.parametrize(
	("value", "unit"),
	[
		(-273.16, "C"),
		(-459.68, "F"),
		(math.inf, "C"),
		(-math.inf, "F"),
		(math.nan, "C"),
	],
)
def test_validate_temperature_rejects_invalid_numeric_values(value, unit):
	assert validate_temperature(value, unit) is False


@pytest.mark.parametrize("value", ["25", None, [], {}, True, False])
def test_validate_temperature_rejects_invalid_value_types(value):
	assert validate_temperature(value, "C") is False


@pytest.mark.parametrize("unit", ["K", "", "celsius", None, 1, " C F "])
def test_validate_temperature_rejects_invalid_units(unit):
	assert validate_temperature(25, unit) is False
