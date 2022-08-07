def create_message(s):
    stack = [s]
    def func(s=None):
        if s:
            stack.append(s)
            return func
        else:
            return " ".join(stack)
    return func

print(create_message("Hello")("World!")("how")("are")("you?")())