"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3

def test_sub_resta_negativa():
    """Test: restar un número mayor al primero (resultado negativo)."""
    assert sub(2, 5) == -3


def test_sub_restar_cero():
    """Test: restar cero."""
    assert sub(10, 0) == 10


def test_sub_dos_numeros_negativos():
    """Test: restar dos números negativos."""
    assert sub(-5, -2) == -3


@pytest.mark.parametrize("a,b,resultado", [
    (5.5, 2.3, 3.2),
    (10.7, 3.2, 7.5),
    (1.1, 0.5, 0.6),
])
def test_sub_numeros_decimales(a, b, resultado):
    """Test: restar dos números decimales (float)."""
    assert abs(sub(a, b) - resultado) < 1e-9
