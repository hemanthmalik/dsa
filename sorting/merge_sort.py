mylist = [1,4,2,53,234,6,415,-5,345,3]

def merge(left_arr, right_arr): # O(nlogn) O(n)
    merged_arr = []
    l, r = len(left_arr), len(right_arr)
    i, j = 0, 0
    while (i < l) and (j < r):
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        elif left_arr[i] > right_arr[j]:
            merged_arr.append(right_arr[j])
            j += 1
    merged_arr += left_arr[i:] if i != l else right_arr[j:]
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        L = merge_sort(arr[:mid])
        R = merge_sort(arr[mid:])
        return merge(L, R)

print(merge_sort(mylist))