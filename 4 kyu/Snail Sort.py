def snail(snail_map):
    matrix = [row[:] for row in snail_map]
    arr = []
    while matrix:
        for i in matrix[0]:
            arr.append(i)
        matrix.pop(0)
        if not matrix:
            break
        for j in range(len(matrix)):
            arr.append(matrix[j].pop(-1))
        for k in matrix[-1][::-1]:
            arr.append(k)
        matrix.pop(-1)
        for l in range(len(matrix))[::-1]:
            arr.append(matrix[l].pop(0))
    return arr




def snail(snail_map):
    matrix = [row[:] for row in snail_map]
    arr = []
    while matrix:
        arr += [*matrix.pop(0)]
        if not matrix:
            break
        arr += [matrix[j].pop(-1) for j in range(len(matrix))]
        arr += [k for k in matrix[-1][::-1]]
        matrix.pop(-1)
        arr += [matrix[j].pop(0) for j in range(len(matrix))[::-1]]
    return arr
