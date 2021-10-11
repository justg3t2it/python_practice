import pytest
from fibonacci import fibby

def testFirst():
    assert fibby(1) == 1

def testZero():
    assert fibby(0) == 0

def testOther():
    assert fibby(5) == 5

def testEight():
    assert fibby(8) == 21

def testNegative():
    assert fibby(-5) == 1


