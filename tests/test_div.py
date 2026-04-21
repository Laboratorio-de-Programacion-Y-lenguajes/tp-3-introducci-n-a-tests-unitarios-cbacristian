"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div

# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0

#   - División que da resultado decimal (float)
def test_div_decimal():
    """División que da resultado decimal: 5 / 2 debe dar 2.5."""
    assert div(5, 2) == 2.5

#   - División con números negativos
def test_div_negativos():
    """División con números negativos."""
    assert div(-10, 2) == -5.0
    assert div(10, -2) == -5.0
    assert div(-10, -2) == 5.0

#   - División por cero → debe lanzar ZeroDivisionError
def test_div_por_cero():
    """División por cero debe lanzar ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        div(10, 0)

