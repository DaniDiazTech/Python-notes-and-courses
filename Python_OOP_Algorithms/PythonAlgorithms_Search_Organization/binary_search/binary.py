import random as rm

def binary_search(orderer_list, first_index, last_index, objective):
    print(f"Searching for {objective} between {orderer_list[first_index]} and {orderer_list[last_index - 1]}")
    try:    
        if first_index > last_index:
            return False
        
        middle = (first_index + last_index) // 2

        if orderer_list[middle] == objective:
            return True
        elif orderer_list[middle] < objective:
            return binary_search(orderer_list, middle + 1, last_index, objective)
        elif orderer_list[middle] > objective:
            return binary_search(orderer_list, first_index, middle - 1, objective)
    except IndexError as i:
        pass
        


def main():
    list_size = int(input("What's your list size >> "))
    objective = int(input("What number you want to find? >> "))

    random_list = sorted([rm.randint(0, 100) for i in range(list_size)])
    
    found = binary_search(random_list, 0, len(random_list), objective) 
    
    print(random_list)
    print(f"Your objective number :{objective},  {'was found' if found else 'was not found'} in the list")


if __name__ == "__main__":
    main()    

