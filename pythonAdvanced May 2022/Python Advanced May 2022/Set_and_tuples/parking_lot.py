
license_plates = set()

for _ in range(int(input())):
    command = input().split(', ')
    direction = command[0]
    plate_number = command[1]

    if direction == "IN":
        license_plates.add(plate_number)
    else:
        license_plates.discard(plate_number)
if len(license_plates) > 0:
    for license_plate in license_plates:
        print(license_plate)
else:
    print("Parking Lot is Empty")
