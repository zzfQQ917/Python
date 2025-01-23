def Hello():
    print("Hello, World!")
Hello()

def add_numbers(num1,num2):
    addition = num1+num2
    return addition
add_numbers(1,2)

def triple(num1,num2,num3):
    list1 = [num1,num2,num3]
    highest_num = max(list1)
    return highest_num
triple(1,2,3)

def highest_lowestoflist(list1):
    lowest = min(list1)
    highest = max(list1)
    return lowest,highest
highest_lowestoflist(list1 = [1,2])

def str_indexing(str_var,num1):
    return str_var[num1]
str_indexing("니하오. ",1)