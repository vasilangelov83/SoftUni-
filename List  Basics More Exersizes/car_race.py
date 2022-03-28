

numbers = list(map(int,input().split(" ")))

car_left = 0
car_right = 0
track = len(numbers) - 1
half_track = int(track/2)

for i in range(half_track):
    if numbers[i] == 0:
        car_left *= 0.8
    else:
        car_left += numbers[i]

for j in range(-1,-half_track-1,-1):

    if numbers[j] == 0:
        car_right *= 0.8
    else:
        car_right += numbers[j]

if car_right > car_left:
    print(f"The winner is left with total time: {car_left:.1f}")
else:
    print(f"The winner is right with total time: {car_right:.1f}")
