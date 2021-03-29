def bubble_sort(n, arr):
    swaps = 0
    for i in range(n-1):
        swap = False
        for j in range(n-1):
            if int(arr[j+1]) < int(arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
                swaps += 1
        if not swap:
            return swaps

n = 5
arr = '21 12 3 94 5'.split(" ")

print(bubble_sort(n, arr))
print(arr)