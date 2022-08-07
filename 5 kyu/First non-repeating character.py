def first_non_repeating_letter(string):
    new_list = list(string.lower())
    for i, l in enumerate(new_list):
        if new_list.count(l) == 1:
            return string[i]
    return ''
        


    # for l in new_list:
    #     print(l, [val for val in new_list])
    #     if any(l == val for val in new_list):
    #         new_list = [val for val in new_list if l != val]

print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('moonmen'))

print(first_non_repeating_letter(''))

print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))

print(first_non_repeating_letter('~><#~><'))
print(first_non_repeating_letter('hello world, eh?'))

print(first_non_repeating_letter('sTreSS'))
print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))