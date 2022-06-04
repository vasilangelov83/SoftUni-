

n, m = [int(x) for x in input().split(", ")]
matrix = []
result = 0
for _ in range(n):
    line = [int(x) for x in input().split(", ")]
    result += sum(line)
    matrix.append(line)
print(result)
print(matrix)
