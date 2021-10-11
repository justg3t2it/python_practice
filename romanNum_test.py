import pytest
from romanNum import roman


def testFirst():
    assert roman("LV") == 55

def testSecond():
    assert roman("CL") == 150

def testThird():
    assert roman("CXXXVII") == 137

def testFourth():
    assert roman("IC") == 99


