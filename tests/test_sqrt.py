"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
def test_sqrt_cero():
    """Test: la raíz de 0 debe dar 0.0."""
    assert sqrt(0) == 0.0


def test_sqrt_no_cuadrado_perfecto():
    """Test: la raíz de un número que no es cuadrado perfecto da resultado decimal."""
    assert sqrt(2) == pytest.approx(1.414213562, rel=1e-6)


def test_sqrt_negativo():
    """Test: la raíz de un número negativo debe lanzar ValueError."""
    with pytest.raises(ValueError):
        sqrt(-4)
