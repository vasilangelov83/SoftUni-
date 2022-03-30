import re

participants = input().split(", ")
runners_dict = dict()

command = input()
max_distance = 0
while command != "end of race":

    pattern = r"([A-Za-z]*)([0-9]*)"
    matches = re.finditer(pattern,command)
    name = ""
    number = ""
    distance = 0
    for match in matches:
        if match[1] is not None:
            name += match.group(1)

        if match[2] is not None and match[2] != '':
            number += match.group(2)
    for num in number:
        distance += int(num)
    if name in runners_dict:
        runners_dict[name] += distance
    else:
        if name in participants:
            runners_dict[name] = distance
    command = input()
sorted_dict = sorted(runners_dict.items(), key=lambda x: x[1], reverse= True)


print(f"1st place: {sorted_dict[0][0]}")
print(f"2nd place: {sorted_dict[1][0]}")
print(f"3rd place: {sorted_dict[2][0]}")



