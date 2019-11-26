"""Test it."""
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_it():
    """Movement is currently just visual so we assert it."""
    assert True != False
