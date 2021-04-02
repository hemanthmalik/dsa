'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
count = 0
# Write your code here
def merge_sort(arr):
    arr_size = len(arr)
    if arr_size <= 1:
        return arr
    mid = arr_size//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, mid, right, arr_size-mid)

def merge(left, l, right, r):
    i = j = 0
    merged_arr = []
    while i < l and j < r:
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
            global count
            count += l-i
            
    merged_arr += left[i:] if i < l else right[j:]
    return merged_arr

f = open("/Downloads/mrg.txt", "r")
print(f.readline()) 
arr = tuple(map(int, f.readline().split(" ")))
merge_sort(arr)
print(count)