from collections import deque

water_quantity = int(input())

water_queue = deque()

name = input()

while name != "Start":
    water_queue.append(name)
    name = input()
name = input()
while name != "End":
    if name.isdigit():
        if int(name) <= water_quantity:
            water_quantity -= int(name)
            print(f"{water_queue.popleft()} got water")
        else:
            print(f"{water_queue.popleft()} must wait")
    else:
        _, liters = name.split()
        water_quantity += int(liters)
    name = input()
print(f"{water_quantity} liters left")
