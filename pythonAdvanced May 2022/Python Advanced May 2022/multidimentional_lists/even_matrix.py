

n = int(input())
even_matrix = []

for _ in range(n):
    line = [int(x) for x in input().split(', ') if int(x) % 2 == 0 ]
    even_matrix.append(line)
print(even_matrix)