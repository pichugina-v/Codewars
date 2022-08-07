def add(n):
    return CustomAdd(n)

class CustomAdd(int):
    def __call__(self, n):
        return add(self + n)


print(add(1))
print(add(1)(2))
print(add(1)(2)(3))
