def factorial(n):
    """
        Calculate the n factorial
        
        n == int, n > 0
    
        returns n!
    """
    print(str(n), "operation")
    if n == 1:
        return 1
    
    return n * factorial(n - 1)
    
n = int(input("Type the number >> "))

print(factorial(n))
