import sys, os
sys.path.append(os.path.dirname(__file__))

from calc import add

def test_add_two_numbers():
    result = add(2, 3)
    assert result == 5
