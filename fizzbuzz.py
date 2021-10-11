def fizzybuzzy(n): 
        try: 
            n = int(n)
            
            if (n % 3 == 0):
                return "Fizz"
            if (n % 5 == 0):
                return "Buzz" 
            else: 
                return n 
        except:
             raise ValueError("Not an integer / invalid input found")
        
    
        

        

