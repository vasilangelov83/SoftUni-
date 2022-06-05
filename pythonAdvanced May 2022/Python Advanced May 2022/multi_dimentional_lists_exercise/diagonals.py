
n = int(input())

matrix = [
    [int(x) for x in input().split(", ")] for _ in range(n)
]
primary_diagonal = []
secondary_diagonal = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            primary_diagonal_sum += matrix[i][j]
            primary_diagonal.append(str(matrix[i][j]))
        if i == n - j -1:
            secondary_diagonal_sum += matrix[i][j]
            secondary_diagonal.append(str(matrix[i][j]))
print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {secondary_diagonal_sum}")