def binary_search(item, arr): # O(log n) O(1)
    lower = 0
    upper = len(arr)
    while upper >= lower:
        median = (lower + upper)//2
        if item > arr[median]:
            lower = median + 1
        elif item < arr[median]:
            upper = median - 1
        else:
            return median
    return -1
    

item = int(input('Enter no. that you want to search --> '))
arr = [123,33,45,6,34,23,98,788,80,78,56,-4,345]
arr.sort()
print(binary_search(item, arr))