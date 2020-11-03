import time

def f(x):
    result = 0
    for i in range(x):
        for j in range(x):
            for l in range(x):
                result += 1
    
    start = time.time()        
    print(result)
    end = time.time()
    print(f"Time 1 {end - start}")
    start2 = time.time()
    print(x ** 3)
    end2 = time.time()
    print(f"Time 2 {end2 - start2}") 

while True:
    f(int(input("Cubic number >> ")))
