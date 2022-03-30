

data = input().split(" ")
num = int(input())
data = list(map(int, data))
people = data
permutation_list = []
counter = 0
offset = 0
while people:
    for i in range(len(people)):
        counter += 1

        if counter == num:
            permutation_list.append(people[i-offset])
            people.pop(i-offset)
            offset += 1
            counter = 0
    offset = 0
permutation_list = list(map(str, permutation_list))
print(f"[{','.join(permutation_list)}]")


