
stack = []
n = int(input())
for _ in range(n):

    command = input()
    if command[0] == "1":
        command = command.split()
        stack.append(int(command[1]))
    elif command == "2":
        stack.pop()
    elif command == "3":
        if len(stack) != 0:
            print(max(stack))
    elif command == "4":
        if len(stack) != 0:
            print(min(stack))
for element in range(len(stack)):
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())
