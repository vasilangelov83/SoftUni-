

command = input().split(" ")
animals_dict = {}
animal_by_area = {}
while command[0] != "EndDay":

    if command[0] == "Add:":
        new_command = command[1].split("-")
        name = new_command[0]
        needed_food = int(new_command[1])
        area = new_command[2]
        if name not in animals_dict:
            animals_dict[name] = [needed_food, area]
            if area not in animal_by_area:
                animal_by_area[area] = [name]
            else:
                animal_by_area[area].append(name)
        else:
            animals_dict[name][0] += needed_food

    elif command[0] == "Feed:":
        new_command = command[1].split("-")
        name = new_command[0]
        food = int(new_command[1])
        if name in animals_dict:
            animals_dict[name][0] -= food
            area = animals_dict[name][1]
            if animals_dict[name][0] <= 0:
                animals_dict.pop(name)
                print(f"{name} was successfully fed")
                animal_by_area[area].remove(name)
                if len(animal_by_area[area]) == 0:
                    animal_by_area.pop(area)
    command = input().split(" ")
print("Animals:")
for animal in animals_dict:
    print(f" {animal} -> {animals_dict[animal][0]}g")
print("Areas with hungry animals:")
for area in animal_by_area:
    print(f" {area}: {len(animal_by_area[area])}")
