import random as rm
import time as t

def linear_search(objective, list_for_search, iter_lin=0):
    start = t.time()
    match = False

    for element in list_for_search: # O(n)
        iter_lin += 1
        if element == objective:
            match = True
            break
    end = t.time()
    total_l_time = (end - start)

    return match, iter_lin, total_l_time

def binary_search(orderer_list, first_index, last_index, objective, iter_bin=0):
    iter_bin += 1 
    if first_index > last_index:
        return False
    
    middle = (first_index + last_index) // 2

    if orderer_list[middle] == objective:
        return True
    elif orderer_list[middle] < objective:
        return binary_search(orderer_list, middle + 1, last_index, objective),iter_bin
    elif orderer_list[middle] > objective:
        return binary_search(orderer_list, first_index, middle - 1, objective), iter_bin



def main():
    list_size = int(input("What's your list size >> "))
    objective = int(input("What number you want to find? >> "))

    random_list = sorted([rm.randint(0, 100) for i in range(list_size)])
    
    found, iter_bin = binary_search(random_list, 0, len(random_list), objective) 
    found, iter_lin, time = linear_search(objective, random_list)

    # print(f"Searching for {objective} between {orderer_list[first_index]} and {orderer_list[last_index - 1]}")
    print(random_list)
    print(f"Linear search iterations = {iter_lin}")
    print(f"Time taken for linear iterations: {time}")
    print(f"Binary search iterations = {iter_bin}")
    print(f"Your objective number :{objective},  {'was found' if found else 'was not found'} in the list")


if __name__ == "__main__":
    main()    


