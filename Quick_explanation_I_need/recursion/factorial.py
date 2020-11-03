
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n  - 1) 


def main():
    print(factorial(int(input("What factorial do you want? >> "))))

if __name__ == "__main__":
    main()
