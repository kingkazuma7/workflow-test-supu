import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from add import add, multiply


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(5, -3) == 2


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
