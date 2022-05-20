from collections import deque

number_of_pumps = int(input())

pumps = deque()

for _ in range(number_of_pumps):

    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for pump_station_number in range(number_of_pumps):
    tank_level = 0
    failed = False
    for fuel, distance in pumps:
        tank_level += fuel
        if distance > tank_level:
            failed = True
            break
        else:
            tank_level -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(pump_station_number)
        break
