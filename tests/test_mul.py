"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12

@pytest.mark.parametrize("a,b,esperado", [
    # Multiplicación por cero
    (5, 0, 0),
    (0, 5, 0),
    # Multiplicación de dos números negativos (resultado positivo)
    (-3, -4, 12),
    # Multiplicación de un positivo y otro negativo (resultado negativo)
    (3, -4, -12),
    (-3, 4, -12),
    # Multiplicación por 1 (elemento neutro)
    (5, 1, 5),
    (1, 5, 5),
    # Multiplicación de dos decimales (float)
    (2.5, 4.0, 10.0),
    (3.5, 2.5, 8.75),
])
def test_mul_casos(a, b, esperado):
    """Tests para varios casos de multiplicación."""
    assert mul(a, b) == esperado
