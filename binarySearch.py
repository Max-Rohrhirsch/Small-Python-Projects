def binarrySearch(array, item):
    begin = 0
    end = len(array)-1

    while begin <= end:
        midpoint = begin + (end-begin) // 2
        midpointValue = array[midpoint]
        if midpointValue == item:
            return midpoint
        elif item < midpoint:
            end = midpoint - 1
        else:
            begin = midpoint + 1
    return None


arr = [2,3,4,5,6,7,8,9,10,11,12]
itemA = 7
print(binarrySearch(arr,itemA))
