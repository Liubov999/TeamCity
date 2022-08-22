import pytest

pytest


def test_sum():
    a = 2
    b = 2
    count = a+b
    assert count == 4, f' 4 \n Actual: {count}'


def test_min():
    a = 2
    b = 1
    count = a-b
    assert count == 1, f' 1 \n Actual: {count}'
    
def test_new():
    a = 3
    b = 1
    count = a-b
    assert count == 2, f' 1 \n Actual: {count}'
    

    
    
    
