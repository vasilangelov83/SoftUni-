import re
txt = input()
pattern = r"[a-z]+[-_.]?\w+@\w+\-?\w+\.\w+\.?\w+"

result = re.findall(pattern,txt)

print("".join(result))
