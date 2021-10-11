def fibby(n): 
    n = int(n)
    if n < 0: 
        print("Negative numbers? Who do you think I am? Try again next month.")
    
    if n <= 1: 
        return n
    else: 
        return(fibby(n-1) + fibby(n-2))
        
    n_range = n
    
    for i in range(n_range):
            return fibby(i)

