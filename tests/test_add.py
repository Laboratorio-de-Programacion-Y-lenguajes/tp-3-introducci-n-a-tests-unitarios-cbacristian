"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3

#   - Sumar dos números negativos
def test_add_suma_negativos():
    """Test para sumar dos números negativos."""
    assert add(-5, -3) == -8

#   - Sumar un número positivo y uno negativo
def test_add_positivo_negativo():
    """Test para sumar un número positivo y uno negativo."""
    assert add(5, -3) == 2

#   - Sumar con cero
@pytest.mark.parametrize("a,b,expected", [
    (5, 0, 5),           # positivo + cero
    (0, 5, 5),           # cero + positivo
    (-3, 0, -3),         # negativo + cero
    (0, -3, -3),         # cero + negativo
    (0, 0, 0),           # cero + cero
])
def test_add_con_cero(a, b, expected):
    """Test para verificar la suma con cero."""
    assert add(a, b) == expected

#   - Sumar dos números decimales (float)
@pytest.mark.parametrize("a,b,expected", [
    (1.5, 2.3, 3.8),           # dos decimales positivos
    (0.1, 0.2, 0.3),           # decimales pequeños
    (-1.5, -2.3, -3.8),        # dos decimales negativos
    (5.5, -3.2, 2.3),          # decimal positivo + decimal negativo
    (0.0, 3.14, 3.14),         # cero + decimal
])
def test_add_decimales(a, b, expected):
    """Test para verificar la suma de dos números decimales (float)."""
    assert add(a, b) == pytest.approx(expected)

