import pytest
from anagrams import anagram

def testFirst():
    assert anagram("cat", "tac") == True

def testSecond():
    assert anagram("bad", "dad") == False

def testThird():
    assert anagram(123, "wow") == "error: please enter a proper string input"


