import re
split_pattern = r' *,{1} *'
text = re.split(split_pattern,input())

for name in sorted(text):
    pattern = r"([^0-9+\-.,*/]{0,1})([+-]?[0-9]+\.?[0-9]*)*((\*|\/){0,1})"

    matches = re.finditer(pattern, name)
    daemon_name = name
    daemon_health = 0
    daemon_damage = 0
    arithmetic_ops = []
    for match in matches:
        if match.group(1) is not None and match.group(1) != "":
            daemon_health += ord(match.group(1))

        if match.group(2) is not None and match.group(2) != "":
            daemon_damage += float(match.group(2))
        if match.group(3) is not None and match.group(3) != "":
            arithmetic_ops.append(match.group(3))
    for ch in arithmetic_ops:
        if ch == "*":
            daemon_damage *= 2
        else:
            daemon_damage /= 2
    print(f"{daemon_name} - {daemon_health} health, {daemon_damage:.2f} damage")


