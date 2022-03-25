

key = input()
command = input().split(">>>")
new_key = key
while command[0] != "Generate":
    if command[0] == "Contains":
        current = new_key
        substring = command[1]
        if substring in current:
            print(f"{current} contains {substring}")
        else:
            print("Substring not found!")
    if command[0] == "Flip":
        case = command[1]
        start = int(command[2])
        end = int(command[3])
        current = new_key
        substring = current[start:end]
        if case == "Upper":
            substring = substring.upper()
        else:
            substring = substring.lower()
        new_key = current[:start] + substring + current[end:]
        print(new_key)
    if command[0] == "Slice":
        current = new_key
        start = int(command[1])
        end = int(command[2])
        new_key = current[:start] + current[end:]
        print(new_key)
    command = input().split(">>>")
print(f"Your activation key is: {new_key}")