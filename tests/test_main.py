"""Tests for the main module."""

import pytest
from main import add_numbers, subtract_numbers
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_subtract_numbers():
    """Test the subtract_numbers function."""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 5) == -5
    assert subtract_numbers(-3, -3) == 0
