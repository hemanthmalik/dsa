def quick_sort(arr, l, r): # T(n)=O(n) S(n)=O(1)
    if r-l <= 1:
        return arr
    
    yellow = green = l+1
    while green < r:
        if arr[green] <= arr[l]:
            arr[yellow], arr[green] = arr[green], arr[yellow]
            yellow += 1
        green += 1
    arr[l], arr[yellow-1] = arr[yellow-1], arr[l]

    quick_sort(arr, l, yellow-1)
    quick_sort(arr, yellow, r)


mylist = list(range(100, 0, -1))
quick_sort(mylist, 0, len(mylist))
print(mylist)