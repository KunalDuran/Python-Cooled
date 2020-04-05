# Task is to write a function that check whether the number is and returns
# 'Even' or 'Odd'




# The conventional method
def even_or_odd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'



# One liner
def even_or_odd(n):
    return 'Even' if n % 2 == 0 else 'Odd'
