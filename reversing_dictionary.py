## Making key value and vice versa

numbers = {'one':1, 'two':2, 'three':3}
dict((value, key) for (key, value) in numbers.items())
