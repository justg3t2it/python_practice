import pytest
from fizzbuzz import fizzybuzzy


def testFirst():
    assert fizzybuzzy(36) == "Fizz"

def testSecond():
    assert fizzybuzzy(107) == 107

def testThird():
    assert fizzybuzzy(25) == "Buzz"

def testFourth():
    assert fizzybuzzy(100) == "Buzz"

def testFifth():
    assert fizzybuzzy("int").raises