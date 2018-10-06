import numpy as np 
import random as r
def insertionSort(array): 
     for j in range(1,len(array)):
         key = array[j]
         i = j-1
         while (i > -1) and key < array[i]:
             array[i+1] = array[i]
             i=i-1
         array[i+1] = key
     return array


start = r.randint(1, 1000)
end = r.randint(1, 1000)
size = r.randint(1, 1000)
x = np.random.randint(start, end+start, size+end)
print(insertionSort(x))


