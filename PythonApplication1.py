import numpy as np 
import random as r
from timeit import Timer

def insertionSort(array): 
     for j in range(1,len(array)):
         key = array[j]
         i = j-1
         while (i > -1) and key < array[i]:
             array[i+1] = array[i]
             i=i-1
         array[i+1] = key
     return array


start = r.randint(1, 100)
end = r.randint(1, 100)
size = r.randint(1, 100)
x = np.random.randint(start, end+start, size+end)
t = Timer(lambda: insertionSort(x))
print(t.timeit(number=1))
print(insertionSort(x))


