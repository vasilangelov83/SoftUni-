import re


n = int(input())

attacked_planets = []
destroyed_planets = []
for i in range(n):
    text = input()
    star_list = []
    pattern = r"(s{0,1})(t{0,1})(a{0,1})(r{0,1})"

    matches = re.finditer(pattern,text, flags= re.IGNORECASE)

    for match in matches:
        if match[1] != "":
            star_list.append(match[1])
        if match[2] != "":
            star_list.append(match[2])
        if match[3] != "":
            star_list.append(match[3])
        if match[4] != "":
            star_list.append(match[4])

    decrypted_message = ""
    for ch in text:
        decrypted_message += chr(ord(ch) - len(star_list))
    pattern_2 = r"@([A-Za-z]+)[^A-Za-z@\-!:>]?:([0-9]+)[^a-z@\-!:>]?!(A|D)![^a-z@\-!:>]?->([0-9]+)[^A-Za-z@\-!:>]?"
    catches = re.finditer(pattern_2,decrypted_message)

    for catch in catches:
        planet_name = catch[1]
        population = int(catch[2])
        attack_type = catch[3]
        soldier_count = int(catch[4])

        if attack_type == "A":
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet1 in sorted(destroyed_planets):
    print(f"-> {planet1}")

