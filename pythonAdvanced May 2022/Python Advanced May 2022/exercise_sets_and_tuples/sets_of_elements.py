
unique_nums_of_elements = [int(x) for x in input().split()]
set1 = set(input() for x in range(unique_nums_of_elements[0]))
set2 = set(input() for x in range(unique_nums_of_elements[1]))
set3 = set1.intersection(set2)
for element in set3:
    print(element)