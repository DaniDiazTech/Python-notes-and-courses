import random as rm


def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

def main():
    list_size = int(input("What's your list size >> "))
    objective = int(input("What number you want to find? >> "))

    random_list = [rm.randint(0, 100) for i in range(list_size)]
    
    print(random_list)

    ordered_list = bubble_sort(random_list)

    print(ordered_list)
if __name__ == "__main__":
    main()    

