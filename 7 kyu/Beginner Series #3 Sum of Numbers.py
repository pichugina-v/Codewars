def get_sum(a,b):
    limits = [a, b]
    result = 0
    for i in range(min(limits), max(limits) + 1):
        result += i
    return result
    
print(get_sum(-1, 0))