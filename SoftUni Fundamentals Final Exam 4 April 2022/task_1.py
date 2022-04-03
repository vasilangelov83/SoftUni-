

user_pass = input()
command = input().split(" ")
while command[0] != "Complete":
    if command[0] == "Make":
        if command[1] == "Upper":
            index = int(command[2])
            user_pass = user_pass[:index] + user_pass[index].upper() + user_pass[index+1:]
            print(user_pass)

        elif command[1] == "Lower":
            index = int(command[2])
            user_pass = user_pass[:index] + user_pass[index].lower() + user_pass[index+1:]
            print(user_pass)
    elif command[0] == "Insert":
        index = int(command[1])
        char = command[2]
        if index < len(user_pass):
            user_pass = user_pass[:index] + char + user_pass[index:]
            print(user_pass)
    elif command[0] == "Replace":
        current = user_pass
        char = command[1]
        if char in user_pass:
            value = int(command[2])
            new_char = chr(ord(char) + value)
            current = current.replace(char, new_char)
            user_pass = current
            print(user_pass)
    elif command[0] == "Validation":
        upper_counter = 0
        lower_counter = 0
        digit_counter = 0
        if len(user_pass) < 8:
            print("Password must be at least 8 characters long!")
        for ch in user_pass:
            if ch.isalnum() or ch == "_":
                pass
            else:
                print("Password must consist only of letters, digits and _!")
            if ch.isupper():
                upper_counter += 1
            elif ch.islower():
                lower_counter += 1
            elif ch.isdigit():
                digit_counter += 1
        if upper_counter < 1:
            print("Password must consist at least one uppercase letter!")
        if lower_counter < 1:
            print("Password must consist at least one lowercase letter!")
        if digit_counter < 1:
            print("Password must consist at least one digit!")
    command = input().split(" ")