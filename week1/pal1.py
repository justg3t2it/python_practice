"""Read the same as left to right, right to left
>>>Accounting for cases where:
string has punctuation
string has white spaces

Used regex to remove punctuation in the string for more accurate results
"""


import string
import re                            

def isPal1(s):
    s = s.lower()
    res = re.sub(r'[^\w]', '', s)
    res = res.replace(" ", "")

    # ^ match anything that is not these things
    # \w anything that is alpha numeric
    # \s white space
    # assign to white space ''


    return res == res[::-1]


str1 = "racecar"
str2 = "Ha!n^nah?"
str3 = "computer"

print(isPal1(str1))
print(isPal1(str2))
print(isPal1(str3))
