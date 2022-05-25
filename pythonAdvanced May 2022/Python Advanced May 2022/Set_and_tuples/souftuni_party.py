
reservation_codes = set()

for _ in range(int(input())):
    reservation_codes.add(input())
while True:
    command = input()
    if command == "END":
        break
    else:
        reservation_codes.discard(command)
vip_guests = list()
print(len(reservation_codes))
for code in reservation_codes:
    if code[0].isdigit():
        vip_guests.append(code)

for guest in sorted(vip_guests):
    print(guest)

for regular_guest in sorted(reservation_codes):
    if regular_guest not in vip_guests:
        print(regular_guest)

