"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean

# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
def test_mean_un_elemento():
    """Test para lista con un solo elemento."""
    assert mean([5]) == 5.0

def test_mean_negativos():
    """Test para lista con números negativos."""
    assert mean([-1, -2, -3]) == -2.0

def test_mean_decimales():
    """Test para lista con números decimales."""
    assert mean([1.5, 2.5, 3.5]) == 2.5

def test_mean_vacia():
    """Test para lista vacía, debe lanzar ValueError."""
    with pytest.raises(ValueError):
        mean([])
