import random as rm

def linear_search(objective, list_for_search):
    match = False

    for element in list_for_search: # O(n)
        if element == objective:
            match = True
            break
    
    return match


def main():
    list_size = int(input("What's your list size >> "))
    objective = int(input("What number you want to find? >> "))

    random_list = [rm.randint(0, 100) for i in range(list_size)]
    found = linear_search(objective, random_list)
    print(random_list)
    print(f"Your objective number :{objective},  {'was found' if found else 'was not found'} in the list")


if __name__ == "__main__":
    main()    

