from itertools import combinations

# def bananas(s) -> set:
    # result = set()
    # target = 'banana'
    # i = 0
    # resulting_word = ['-'] * len(s)
    # for n, letter in enumerate(s):
    #     while i <= len(s):
    #         if s[n] == target[i]:
    #             resulting_word[n] = letter
    #         i += 1
    #         # print(resulting_word)
    #     else:
    #         break
    # result.add(''.join(resulting_word))
    # print(result)
    # return result

def bananas(s) -> set:
    result = set()
    target = 'banana'
    
    def insert_dash(index, lst):
        return lst.insert(index, '-')

# print(bananas("banann"))
# print(bananas("banana"))
# print(bananas("bbananana"))
print(bananas("bananaaa"))
# print(bananas("bananana"))