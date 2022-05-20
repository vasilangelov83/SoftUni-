

string_stack = [str(x) for x in input()]
for _ in range(len(string_stack)):
    print(string_stack.pop(), end="")