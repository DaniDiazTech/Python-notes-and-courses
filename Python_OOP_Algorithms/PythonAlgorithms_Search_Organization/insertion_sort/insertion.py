import random as rm

def insetion_sort(my_list):
    n = len(my_list)

    for index in range(1, n):
        current_value = my_list[index]
        current_position = index

        while current_position > 0 and my_list[current_position - 1] > current_value:
            my_list[current_position] = my_list[current_position - 1]
            current_position -= 1
        
        my_list[current_position] = current_value
    
    return my_list

def main():
    size = 5
    fixed_list = [12, 14, 15, 4, 545]
    random_list = [rm.randint(0, 100) for i in range(size)]

    print(insetion_sort(fixed_list))
    print(insetion_sort(random_list))


if __name__ == "__main__":
    main()