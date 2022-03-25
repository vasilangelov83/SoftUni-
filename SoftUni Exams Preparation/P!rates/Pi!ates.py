
cities_dict = {}
while True:
    cities = input().split("||")
    name = cities[0]
    if cities[0] == "Sail":
        break

    population = int(cities[1])
    gold = int(cities[2])
    if name not in cities_dict:
        cities_dict[name] = [population, gold]
    else:
        cities_dict[name][0] += population
        cities_dict[name][1] += gold
while True:
    events = input().split("=>")
    action = events[0]
    if action == "End":
        break
    if action == "Plunder":
        town = events[1]
        people = int(events[2])
        gold = int(events[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities_dict[town][0] -= people
        cities_dict[town][1] -= gold
        if cities_dict[town][0] <= 0 or cities_dict[town][1] <= 0:
            cities_dict.pop(town)
            print(f"{town} has been wiped off the map!")
    if action == "Prosper":
        town = events[1]
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_dict[town][1]} gold.")

print(f"Ahoy, Captain! There are {len(cities_dict.keys())} wealthy settlements to go to:")
if len(cities_dict.keys()) > 0:

    for key in cities_dict:

        print(f"{key} -> Population: {cities_dict[key][0]} citizens, Gold: {cities_dict[key][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

