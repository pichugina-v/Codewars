def anagrams(word, words):
    result = []
    for w in words:
        if sorted(word) == sorted(w):
            result.append(w)
        else:
            continue
    return result
        


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))