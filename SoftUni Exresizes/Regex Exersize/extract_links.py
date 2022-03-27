import re

txt = input()

pattern = r"(www\.[A-Za-z0-9-]+(\.[a-z]+)+(?![a-z(_\-\.]))"

while txt != "":


    result = re.finditer(pattern,txt)

    for match in result:
        print(match[1])
    txt = input()