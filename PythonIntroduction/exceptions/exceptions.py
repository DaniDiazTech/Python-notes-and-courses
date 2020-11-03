def division(list, divisor):
    try:
        return [(i / divisor) for i in list]
    except ZeroDivisionError  as e:
        print(e)
        return "Division by zero, try other divisor"

my_list = [i for i in range(1, 21)]
my_divisor = 0

print(division(my_list, my_divisor))