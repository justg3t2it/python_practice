import pytest
from charType import types

def testFirst():
    assert types("python") == (1 , 5)

def testSecond():
    assert types("vowel") == (2, 3)

def testThird():
    assert types("google") == (3, 3)

def testFourth():
    assert types("liliana") == (4 , 3)

def testFifth():
    assert types("") == (0 , 0)

def testSixth():
    assert types("str&ng") == (0 , 5)

def testSeventh():
    assert types("str1ng") == (0 , 5)

