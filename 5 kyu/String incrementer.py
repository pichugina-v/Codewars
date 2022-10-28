def increment_string(string):
    num = "".join(n for n in string if n.isdigit())
    if len(num) == 0:
        return "".join(n for n in string if not n.isdigit()) + "1"
    string_list = list(string[::-1])
    digital_str = ""
    char_str = ""
    for i, n in enumerate(string_list):
        if str(n).isdigit():
            digital_str += str(n)
        else:
            char_str = ("".join(string_list[i::]))[::-1]
            break
    digital_str = digital_str[::-1]
    num = "".join(n for n in digital_str if n.isdigit())
    if len(num) != len(str(int(num))):
        for i, n in enumerate(list(num)):
            if int(n) != 0:
                return char_str + "".join(n for n in  digital_str if not n.isdigit()) + (str(int(num) + 1).zfill(i + 1))
            return char_str + "".join(n for n in digital_str if not n.isdigit()) + (str(int(num) + 1).zfill(len(num)))
    return char_str + "".join(n for n in digital_str if not n.isdigit()) + str(int(num) + 1)

#     def increment_string(strng):
#         head = strng.rstrip('0123456789')
#         tail = strng[len(head):]
#         if tail == "": return strng+"1"
#         return head + str(int(tail) + 1).zfill(len(tail))

print(increment_string("foo"))
print(increment_string("foobar0001"))
print(increment_string("foobar1"))
print(increment_string("foobar00"))
print(increment_string("foobar99"))
print(increment_string("foobar099"))
print(increment_string(""))
print(increment_string("044"))
print(increment_string("KZ5/19843817528000000627390314"))

# перевернуть строку и дойти до первого с конца символа который isdigit = False