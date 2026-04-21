"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---

@pytest.mark.parametrize("base,exponent,expected", [
    (5, 0, 1),
    (100, 0, 1),
    (-7, 0, 1),
])
def test_pow_exponente_cero(base, exponent, expected):
    """Cualquier número elevado a 0 debe dar 1."""
    assert pow_(base, exponent) == expected


@pytest.mark.parametrize("base,exponent,expected", [
    (5, 1, 5),
    (-3, 1, -3),
    (0, 1, 0),
])
def test_pow_exponente_uno(base, exponent, expected):
    """Número elevado a 1 debe dar el mismo número."""
    assert pow_(base, exponent) == expected


@pytest.mark.parametrize("base,exponent,expected", [
    (-2, 2, 4),
    (-3, 4, 81),
    (-5, 2, 25),
])
def test_pow_base_negativa_exponente_par(base, exponent, expected):
    """Base negativa con exponente par debe dar resultado positivo."""
    assert pow_(base, exponent) == expected


@pytest.mark.parametrize("base,exponent", [
    (9, 0.5),
    (16, 0.5),
    (4, 0.5),
])
def test_pow_exponente_decimal(base, exponent):
    """Potencia con exponente decimal (raíz cuadrada)."""
    assert pow_(base, exponent) == pytest.approx(base ** exponent)
