# Assignment: Vowels and Consonants Count 

Given a word, tell me the vowel and consonant count 

Example: python
Output: 1, 5 

1 = vowel
5 = consonant 

>> Thoughts << 

1. need to traverse through entire string input 
2. need to check if it's a vowel (a, e ,i ,o ,u)
    a. If it is a vowel (matches), increment vowel by 1
    b. If it is not a vowel, must be a consonant, increase consonant by 1 


Edge cases: 
1. What if someone inputs a string like: str1ng? 
2. What is string is null? 
3. What if input is just numeric? 12345 or $%^&&
