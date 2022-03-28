
n = int(input())
heroes_dict = {}
for i in range(n):
    heroes_stats = input().split(" ")
    hero_name = heroes_stats[0]
    hit_points = int(heroes_stats[1])
    if hit_points > 100:
        hit_points = 100
    mana_points = int(heroes_stats[2])
    if mana_points > 200:
        mana_points = 200
    heroes_dict[hero_name] = [hit_points,mana_points]
commands = input().split(" - ")
while commands[0] != "End":
    hero_name = commands[1]
    if commands[0] == "CastSpell":

        mana_points_needed = int(commands[2])
        spell_name = commands[3]
        if heroes_dict[hero_name][1] >= mana_points_needed:
            heroes_dict[hero_name][1] -= mana_points_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    if commands[0] == "TakeDamage":
        damage = int(commands[2])
        attacker = commands[3]

        heroes_dict[hero_name][0] -= damage
        if heroes_dict[hero_name][0] > 0:

            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name][0]} HP left!")
        else:
            heroes_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    if commands[0] == "Recharge":
        amount = int(commands[2])
        current_MP = heroes_dict[hero_name][1]
        if current_MP + amount >= 200:
            amount_recovered = 200 - current_MP
            heroes_dict[hero_name][1] += amount_recovered
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            amount_recovered = amount
            heroes_dict[hero_name][1] += amount_recovered
            print(f"{hero_name} recharged for {amount_recovered} MP!")

    if commands[0] == "Heal":
        amount = int(commands[2])
        current_HP = heroes_dict[hero_name][0]

        if current_HP + amount > 100:
            amount_recovered = 100 - current_HP
            heroes_dict[hero_name][0] += amount_recovered
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            amount_recovered = amount
            heroes_dict[hero_name][0] += amount_recovered
            print(f"{hero_name} healed for {amount_recovered} HP!")


    commands = input().split(" - ")
for key, value in heroes_dict.items():
    print(key)
    print(f"HP: {heroes_dict[key][0]}")
    print(f"MP: {heroes_dict[key][1]}")

