def insertion_sort(n, arr, orig_arr):
    arr_dict = {v: str(i) for i, v in enumerate(arr, 1)}
    for i in range(1, n):
        selected_val, s_index = arr[i], i
        for j in range(i-1, -1, -1):
            if int(arr[j]) > int(selected_val):
                arr[j+1] = arr[j]
                s_index = j
        arr[s_index] = selected_val
    arr_dict = {v: str(i) for i, v in enumerate(arr, 1)}
    return " ".join([arr_dict.get(i) for i in orig_arr])

n = 50
arr = '66 83 29 26 12 3 90 6 68 28 82 58 9 21 22 39 52 1 70 31 15 99 94 50 20 77 48 76 5 87 67 78 69 49 63 57 96 43 79 97 18 100 92 91 14 80 46 61 33 74'.split(" ")

print(insertion_sort(n, arr, arr[:]))