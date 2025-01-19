"""
Test the Calculator class in app.py.
"""

import pytest
from app import Calculator
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_multiply():
    """Test the multiply method of Calculator."""
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, 5) == -5
    assert Calculator.multiply(0, 10) == 0


def test_divide():
    """Test the divide method of Calculator."""
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(9, 3) == 3

    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Calculator.divide(5, 0)
