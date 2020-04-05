import timeit


input_list = range(100)

def divide_by_five(num):
    if num % 5 ==0:
        return True
    else :
        return False

xyz = (i for i in input_list if divide_by_five(i))

print(timeit.timeit('''input_list = range(100)

def divide_by_five(num):
    if num % 5 ==0:
        return True
    else :
        return False

xyz = (i for i in input_list if divide_by_five(i))''' , number = 500))
 
