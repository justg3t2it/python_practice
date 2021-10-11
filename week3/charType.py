import string
import re

def types(st):
    st = st.lower()
    str = re.sub("[^a-zA-Z0-9]", "", st)
    str = re.sub("[0-9]", "", str)
    print(str)
    vowels = 0
    cons = 0
    vowel_dict = {
        "a" : True,
        "e" : True,
        "i" : True,
        "o" : True,
        "u" : True
    }

    if str == "": 
        return (vowels, cons)

    for i in range(len(str)): 
        if str[i] in vowel_dict:
            vowels += 1
        else: 
            cons += 1
        

    return (vowels, cons)
            
        



