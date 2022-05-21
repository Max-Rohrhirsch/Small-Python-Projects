# import numpy as np
# randnums = np.random.randint(1,101,10000).tolist()
number = {9,8,7,6,5,4,3,1,2,0}



def quickSort(array):
    length = len(array)

    if length <= 1:
        return array

    pivot = array.pop()

    greater = []
    lower = []

    for item in array:
        if item > pivot:
            greater.append(item)
        else:
            lower.append(item)
    return quickSort(lower) + [pivot] + quickSort(greater)

# for i in range(10000):
#     quickSort(number)

print(quickSort(number))
