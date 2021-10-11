def roman(st):
    
    if st == "": 
        return st 
        
    num = {
       "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000 
    }
    
    x = 0
    result = 0
    l = len(st)
    
    for char in st:
        result += num[char]
    
    print(result)
    return(result)




