import random as rm 

def merge_sort(lis):
    if len(lis) > 1:
        middle = len(lis) // 2
        left = lis[:middle] # slice from 0 to middle
        right = lis[middle:] # slice from middle to end
        print(left, "*" * 5, right)

    # recursive call of each middle
        
        merge_sort(left)
        merge_sort(right) 

        # iterations for get 2 sublist
        
        i = 0
        j = 0

        # Iterator for the main list
        
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lis[k] = left[i]
                i += 1
            else:
                lis[k] = right[j] 
                j += 1
            
            k += 1

        while i < len(left):
            lis[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lis[k] = right[j]
            j += 1
            k += 1

        print(f"Left : {left}, Right : {right}")
        print(lis)
        print("--" * 50)    

    return lis



def main():
    list_size = int(input("What's your list size >> "))

    random_list = sorted([rm.randint(0, 100) for i in range(list_size)])
    ordered_list = merge_sort(random_list) 

    print(random_list)
    print("-" * 100)
    print(ordered_list)


if __name__ == "__main__":
    main()    


