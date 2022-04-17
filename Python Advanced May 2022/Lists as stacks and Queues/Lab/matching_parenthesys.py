

expression = input()
index_stack = []
for index in range(len(expression)):
    if expression[index] == "(":
        index_stack.append(index)
    elif expression[index] == ")":
        print(expression[index_stack.pop():index+1])
