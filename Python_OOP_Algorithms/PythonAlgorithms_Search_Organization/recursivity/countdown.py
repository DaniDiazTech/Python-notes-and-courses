def countdown(number):
    n = abs(number) # only positive numbers allowed
    n -= 1
    if n > 0:
        print(n)
        countdown(n)
    else: 
        print("BOOOOOM")
    
    print(f"End of function {n}")

countdown(int(input("Your positive number >> ")))
    