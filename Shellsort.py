def shellSort(arr): 
    gap = len(array) // 2
     # loop over the gaps
    while gap > 0:
         # do the insertion sort
         for i in range(gap, len(array)):
             val = array[i]
             j = i
             while j >= gap and array[j - gap] > val:
                 array[j] = array[j - gap]
                 j -= gap
             array[j] = val
         gap //= 2
    return arr

array = [37, 22, 18, 50, 2, 3, 1, 29, 69, 5]
print(shellSort(array))