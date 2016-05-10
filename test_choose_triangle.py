from choose_triangle import *
from choose_triangle_bottomUp_DP import *
from choose_triangle_topDown_DP import *
import pytest

#chooses = [choose_triangle_recursive, choose_triangle_topDown, choose_triangle_bottomUp]
chooses = [choose_triangle_recursive, choose_triangle_topDown]
#chooses = [choose_triangle_recursive]

def test_small_examples():
    for choose in chooses:
        assert choose(1,1) == 1 # only 1 way to get subset of 1
        assert choose(3,1) == 3 # only 3 way to get subset of 3: get 1,2, or 3rd
        assert choose(3,3) == 1 # only 1 way to get subset of 3: get all 1,2, and 3rd
        assert choose(4,2) == 6 # here are subsets: (1,2) (1,3) (1,4) (2,3) (2,4) (3,4)

def test_pascal_triangle():
    triangle = { (0,0) : 1,
        (1,0) : 1, (1,1) : 1,
        (2,0) : 1, (2,1) : 2, (2,2) : 1,
        (3,0) : 1, (3,1) : 3, (3,2) : 3, (3,3) : 1,
        (4,0) : 1, (4,1) : 4, (4,2) : 6, (4,3) : 4, (4,4) : 1,
        (5,0) : 1, (5,1) : 5, (5,2) : 10, (5,3) : 10, (5,4) : 5, (5,5) : 1
    }
    for choose in chooses:
        for nk, res in triangle.items():
            assert choose(*nk) == res

def test_negatives():
    for choose in chooses:
        with pytest.raises(ValueError):
            choose(-1, 100)
    for choose in chooses:
        with pytest.raises(ValueError):
            choose(1, -100)

def test_taking_nothing():
    for choose in chooses:
        assert choose(123, 0) == 1

def test_taking_more_than_have():
    for choose in chooses:
        assert choose(3, 3 + 42) == 0

def test_selecting_1_from_n():
    for choose in chooses:
        for n in range(1, 10):
            assert choose(n, 1) == n

def test_selecting_n_from_n():
    for choose in chooses:
        for n in range(1, 10):
            assert choose(n, n) == 1

@pytest.mark.skip()
def test_poker_hand():
    for choose in chooses:
        assert choose(52, 5) ==  2598960

@pytest.mark.skip()
def test_very_large():
    for choose in chooses:
        choose(1000, 5)
