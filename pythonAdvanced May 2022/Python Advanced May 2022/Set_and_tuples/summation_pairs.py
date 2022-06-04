numbers = [int(x) for x in input().split()]
target = int(input())

list_of_pairs = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            num1 = numbers[i]
            num2 = numbers[j]
            if num1 + num2 == target:
                pair = num1, num2
                list_of_pairs.append(pair)

for pair in sorted(list_of_pairs):

    num1 = pair[0]
    num2 = pair[1]
    print(f"{num1} + {num2} = {target}")



