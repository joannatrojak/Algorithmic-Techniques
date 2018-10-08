import numpy as np
from timeit import Timer
import random as r

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array

def quickSort2(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[r.randint(1, 100)]
        print(pivot)
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array

array = np.random.randint(1, 1000, 10)
print(quickSort(array))
print(quickSort2(array))
t = Timer(lambda: quickSort(array))
s = Timer(lambda: quickSort2(array))
print(t.timeit(number=1))
print(s.timeit(number=1))


