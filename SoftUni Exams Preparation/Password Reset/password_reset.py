

string = input()
new_pass = string

while True:
    command = input()
    if command == "Done":
        break
    if command == "TakeOdd":
        current_pass = new_pass
        new_pass = ""
        for i in range(1, len(current_pass), 2):
            new_pass += current_pass[i]
        print(new_pass)

    command = command.split(" ")
    if command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        new_pass = new_pass[:index] + new_pass[(index+length):]
        print(new_pass)

    if command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in new_pass:
            new_pass = new_pass.replace(substring, substitute)
            print(new_pass)
        else:
            print("Nothing to replace!")
print(f"Your password is: {new_pass}")
