import re

eggs = input()
pattern = r"[@#]+([a-z]{3,})[@#]+[^a-z0-9]*\/+([0-9]+)\/+"
matches = re.finditer(pattern,eggs)
for match in matches:
    color = match[1]
    amount = match[2]
    print(f"You found {amount} {color} eggs!")