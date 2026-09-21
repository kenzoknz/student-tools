import math


ABSOLUTE_ZERO = {
	"C": -273.15,
	"F": -459.67,
}


def validate_temperature(value, unit):
	"""Return whether a temperature value is valid for the given unit."""
	if isinstance(value, bool) or not isinstance(value, (int, float)):
		return False

	if not isinstance(unit, str):
		return False

	normalized_unit = unit.strip().upper()
	if normalized_unit not in ABSOLUTE_ZERO:
		return False

	if not math.isfinite(value):
		return False

	return value >= ABSOLUTE_ZERO[normalized_unit]
