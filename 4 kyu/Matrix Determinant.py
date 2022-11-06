def determinant(matrix, result=0):
    if len(matrix) == 1:
        return matrix[0][0]
    m = [row[:] for row in matrix]
    if len(m) == 2 and len(m[0]) == 2:
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        return det
    for col in list(range(len(m))):
        copy_m = m[1:]
        height = len(copy_m)
        for i in range(height):
            copy_m[i] = copy_m[i][0:col] + copy_m[i][col+1:]
        s = (-1) ** (col % 2)
        print(col, col%2)
        sub_det = determinant(copy_m)
        result += s * m[0][col] * sub_det
    return result

m1 = [[4, 6], [3,8]]
m5 = [[2,4,2],[3,1,1],[1,2,0]]
m8 = [[2, 4, 5, 3, 1, 2],[2, 4, 7, 5, 3, 2],[1, 1, 0, 2, 3, 1],[1, 3, 9, 0, 3, 2],[1, 1, 2, 2, 4, 1],[0, 0, 4, 1, 2, 3]]


print(determinant([[5]]))    # 5
print(determinant(m1))    # 14
print(determinant(m5))    # 10
print(determinant(m8))    # 88
