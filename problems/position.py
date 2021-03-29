def insertion_sort(n, arr):
    for i in range(1, n):
        selected_val, s_index = arr[i], i
        for j in range(i-1, -1, -1):
            if int(arr[j][1]) > int(selected_val[1]):
                arr[j+1] = arr[j]
                s_index = j
        arr[s_index] = selected_val
    return " ".join([str(a[0]) for a in arr])

n = 50
arr = list(enumerate('66 83 29 26 12 3 90 6 68 28 82 58 9 21 22 39 52 1 70 31 15 99 94 50 20 77 48 76 5 87 67 78 69 49 63 57 96 43 79 97 18 100 92 91 14 80 46 61 33 74'.split(" ")))

print(insertion_sort(n, arr))