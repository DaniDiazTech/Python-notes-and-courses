import time

def iteration_factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1

    return answer

def recursive_factorial(n):
    if n == 1:
        return 1
    
    return n * recursive_factorial(n  - 1)

def main():
    n_i = int(input("Iteration number >> "))
    n_r = int(input("Recursive number >> ")) 

    start = time.time()
    
    print(iteration_factorial(n_i))
    
    end = time.time()
    
    print(f"Iteration time = {end - start}")
    
    start2 = time.time()
    
    print(recursive_factorial(n_r))
    
    end2 = time.time()
    
    print(f"Recursive time = {end2 - start2}")


if __name__ == "__main__":
    main()
