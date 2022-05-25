
number_elements = int(input())
elements = [input().split() for el in range(number_elements)]
unique = set()
for group in elements:
    for element in group:
        unique.add(element)

for el in unique:
    print(el)
