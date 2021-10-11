# week2

#Palindrome.py 

> attempts to find the longest palindrome within a string
I used re to make the string lower case and remove punctuation to make sure it addressed 
the following use cases:
   >palindromes with whitespace & palindromes with punctuation in between

# palindrome_test.py 

>tested for different cases using pytest
>testing for empty string
>testing for single character string
>testing for even char in string
>testing for odd char in string
>testing for white space
>testing for punctuation


#Fibonacci.py: 
> Before beginning, rule out negative numbers. I will need to revert back 
to account for them at a later time. 

> Since the first 2 integers equal to themselves:

If 0 return 0 
If 1 return 1 

> After that, return the value of the previous 2 numbers until you reach your entered number 

> returns not prints, you can confirm if right via fibonacci_test.py: 

#Fibonnaci_test.py: 
> tests that first two ints (0 and 1) will return themselves 
> tests the next value that adds the values for the fib numbers before it 

> tests one negative case to make sure negative function is working 
