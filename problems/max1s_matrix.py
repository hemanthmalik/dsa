def max1s(arr): # needs further optimization
    matrix_size = len(arr)
    max1s_row, max1s_val = 0, 0
    for i in range(matrix_size):
        for j in range(matrix_size):
            if arr[i][matrix_size-1-j] == 0:
                break
        if j == matrix_size:
            return i
        elif j > max1s_val:
            max1s_row = i
            max1s_val = j
    return max1s_row


mylist = [[1,0,0,1],
          [0,0,0,1],
          [0,0,1,1],
          [0,0,1,1]]

print(max1s(mylist))
