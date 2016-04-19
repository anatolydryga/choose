from choose_factorial import *
import pytest

def test_small_examples():
        assert choose_factorial(1,1) == 1 # only 1 way to get subset of 1
        assert choose_factorial(3,1) == 3 # only 3 way to get subset of 3: get 1,2, or 3rd
        assert choose_factorial(3,3) == 1 # only 1 way to get subset of 3: get all 1,2, and 3rd
        assert choose_factorial(4,2) == 6 # here are subsets: (1,2) (1,3) (1,4) (2,3) (2,4) (3,4)

def test_negatives():
    with pytest.raises(ValueError):
        choose_factorial(-1, 100)
    with pytest.raises(ValueError):
        choose_factorial(1, -100)

def test_taking_nothing():
    assert choose_factorial(123, 0) == 1

def test_taking_more_than_have():
    assert choose_factorial(3, 3 + 42) == 0

def test_selecting_1_from_n():
    for n in range(1, 10):
        assert choose_factorial(n, 1) == n

def test_selecting_n_from_n():
    for n in range(1, 10):
        assert choose_factorial(n, n) == 1

def test_poker_hand():
    assert choose_factorial(52, 5) ==  2598960

def test_very_large():
    choose_factorial(1000, 5)
