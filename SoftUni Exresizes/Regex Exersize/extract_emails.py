import re
txt = input()
pattern = r"\b(?<![-_.0-9a-z])[A-Za-z0-9]+[._-]?[A-Za-z0-9]+@[A-Za-z0-9]+[._-]*[A-Za-z0-9][._-]?[A-Za-z0-9]*[._-]*[A-Za-z0-9]*[._-][A-Za-z0-9]*\b"

result = re.findall(pattern,txt)

print("".join(result))
