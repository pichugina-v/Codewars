def rotate(matrix, direction):
    arr_len = int([len(l) for l in matrix][0])
    rotated_arr = [] * arr_len
    if direction == "clockwise":
        matrix1 = [row[:] for row in matrix][::-1]
    else:
        matrix1 = [row[:] for row in matrix]
        for j in range(len(matrix1)):
            matrix1[j] = matrix1[j][::-1]
    for j in range(arr_len):
        rotated_arr.append([])
    for j in range(arr_len):
        for i in range(len(matrix1)):
            rotated_arr[j].append(matrix1[i].pop(0))
    return rotated_arr
