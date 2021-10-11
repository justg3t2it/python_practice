"""Read the same as left to right, right to left
>>>Accounting for cases where:
string has punctuation
string has white spaces

Used regex to remove punctuation in the string for more accurate results
"""


import string
import re 
                          
def longestPal(s):
    p_length = 0  # will keep track of the distance between l and r pointers
    pal_length = 0  #longest palindrome legnth
    longest_Palindrome = "" #will store the final palindrome in string
    s = s.lower()
    st = re.sub(r'[^\w]', '', s)
    st = st.replace(" ", "")
    table = [[ 0 for i in range(len(st))] for i in range(len(st))] #table length x length of string


    for p_length in range(0, len(st)):
        left = 0 
        right = left + p_length

    
    
        while right < len(st):
            if left == right: #only one char
                table[left][right] = 1
            else: 
                if st[left] == st[right]: #even use case
                    if left == right -1: #account for start value to stay within range
                        table[left][right] = table[left+1][right-1] + 1
                    else: 
                        table[left][right] = table[left+1][right-1] + 2
                else:
                    table[left][right] = max(table[left+1][right], table[left][right-1])

            if table[left][right] > pal_length:
                pal_length = table[left][right]
                longest_Palindrome = st[left:right+1] #account to stay within range
            

            left += 1
            right += 1

    return longest_Palindrome



    

    

        










    



    


    








