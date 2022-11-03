def solution(array_a, array_b):
    new_array = [(array_a[i] - array_b[i]) for i in range(len(array_a))]
    return sum(map(lambda num: num **2, new_array)) / len(new_array)
