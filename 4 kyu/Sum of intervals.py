def sum_of_intervals(intervals):
    if len(intervals) == 1:
        return intervals[0][1] - intervals[0][0]
    min_val = 0
    max_val = 0
    new_list = []
    for i in intervals:
        if i[0] < min_val:
            min_val = i[0]
        if i[1] > max_val:
            max_val = i[1]
    for i in range(0, max_val - min_val):
        new_list.append(0)
    for i in intervals:
        for j in range(i[0], i[1]):
            new_list[j] = 1
    return sum(new_list)



print(sum_of_intervals([(1, 5), (6, 10)]))
print(sum_of_intervals([(1, 5)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))