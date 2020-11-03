# first example of recursion


i = 0
def greet():
    global i
    i += 1
    print(f"Hello,how it's going : called {i} times")
    if 500 > i:
        greet()    

print(i)

greet()


