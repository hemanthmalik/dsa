'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
count = 0
# Write your code here
def merge_sort(arr, n):
    if n <= 1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid], mid)
    right_size = n-mid
    right = merge_sort(arr[mid:], right_size)
    return merge(left, mid, right, right_size)

def merge(left, l, right, r):
    global count
    i = j = 0
    merged_arr = []
    while i < l and j < r:
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
            count += l-i
            
    merged_arr += left[i:] if i < l else right[j:]
    return merged_arr

f = open("/home/tnameh/Downloads/mrg.txt", "r")
n = int(f.readline())
arr = tuple(map(int, f.readline().split(" ")))
merge_sort(arr, n)
print(count)