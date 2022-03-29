
data = input().split(" ")
num = int(input())
data = list(map(int,data))
people = data
permutation = []
counter = 0
counter_2 = 0



while people:

    for i in range(len(data)):
        counter += 1
        if counter == num:
            permutation.append(people[i])
            counter = 0


    for j in permutation:

        if j in people:
            people.remove(j)
permutation = list(map(str, permutation))
print(f"[{','.join(permutation)}]")


