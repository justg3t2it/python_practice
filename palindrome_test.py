import pytest
from palindrome import longestPal

def testEmpty():
    assert longestPal("") == ""

def testOneChar():
    assert longestPal("a") == "a"

def testOdd():
    assert longestPal("hanna") == "anna"

def testEven():
    assert longestPal("hahah") == "hahah"

def testPunctuation():
    assert longestPal("Dammit I'm mad.") != "dammitimmad."
    #assert longestPal("Dang!") == False

def testWhiteSpace():
    assert longestPal("w ow") == "wow"

 


