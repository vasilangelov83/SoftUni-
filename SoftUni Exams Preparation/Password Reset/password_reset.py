

string = input()
password = ""

while True:
    command = input()
    if command == "Done":
        break
    if command == "TakeOdd":
        for i in range(len(string)):
            if i % 2 != 0:
                password += string[i]
        print(password)

    command = command.split(" ")
    if command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        if index >= 0:
            to_remove = password[index:(index+length)]

        else:
            if index < -1:
                to_remove = password[(index - length):index]

            else:
                to_remove = password[(index - length):index]
        password = password.replace(to_remove, "", 1)
        print(password)

    if command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
print(f"Your password is: {password}")
