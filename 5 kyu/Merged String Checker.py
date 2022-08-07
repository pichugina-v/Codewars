def is_merge(s, part1, part2):
    check = part1 + part2
    if len(check) > len(s):
        return False
    return \
        part1 and part1[0] == s[0] and check_pattern(s[1:], part1[1:], part2) or \
        part2 and part2[0] == s[0] and check_pattern(s[1:], part1, part2[1:]) or \
        False if s else not part1 and not part2

def check_pattern(s, part1, part2):
    return \
        part1 and part1[0] == s[0] and check_pattern(s[1:], part1[1:], part2) or \
        part2 and part2[0] == s[0] and check_pattern(s[1:], part1, part2[1:]) or \
        False if s else not part1 and not part2

# def check_pattern(part, s):
#     result = []
#     for y in s:
#         for i, p in enumerate(part):
#             if y == p:
#                 result.append(i)
#     print(result)
#     for n in range(len(result) - 1):
#         if result[n] < result[n+1]:
#             continue
#         else:
#             return False
#     return True
    

print(is_merge('codewars', 'code', 'wars'))
print(is_merge('codewars', 'cdw', 'oears'))
print(is_merge('codewars', 'cod', 'wars'))
print(is_merge('bananas', 'ba', 'anas'))

# print(check_pattern('codewars', 'cod'))