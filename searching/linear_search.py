def linear_search(item, arr): # O(n) O(1)
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

item = 45
arr = [123,33,45,6,34,23,98,788,80,78,56,-4,345]
print(linear_search(item, arr))