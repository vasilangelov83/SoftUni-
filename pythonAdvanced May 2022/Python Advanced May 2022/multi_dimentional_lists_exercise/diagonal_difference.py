
n = int(input())

matrix = [
    [int(x) for x in input().split(" ")] for _ in range(n)
]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            primary_diagonal_sum += matrix[i][j]

        if i == n - j -1:
            secondary_diagonal_sum += matrix[i][j]
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
