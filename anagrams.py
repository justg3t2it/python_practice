def anagram(a, b):
    if (isinstance(a, str) == True) and (isinstance(b,str) == True):
        if sorted(a) == sorted(b):
            return True
        else: 
            return False
    else:
        error = "error: please enter a proper string input"
        return error