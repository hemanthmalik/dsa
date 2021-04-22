def max1s(arr): # needs further optimization
    matrix_size = len(arr)
    counter_arr = [0 for _ in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            if arr[i][matrix_size-1-j] == 0:
                counter_arr[i] = j
                break
    max1s_row, max1s_val = 0, counter_arr[0]
    for k in range(matrix_size):
        if counter_arr[k] > max1s_val:
            max1s_row = k
    return max1s_row


mylist = [[0,0,1,1],
          [0,0,0,1],
          [0,0,0,1],
          [0,1,1,1]]

print(max1s(mylist))
