

string = list(map(int,input().split(", ")))

zero = []
result = []
for i in range(len(string)):

    if string[i] == 0:
        zero.append(string[i])
    else:
        result.append(string[i])
for num in zero:
    result.append(num)
print(result)
