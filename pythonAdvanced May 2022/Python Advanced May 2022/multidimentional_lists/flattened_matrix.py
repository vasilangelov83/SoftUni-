



n = int(input())

matrix = [input().split(', ') for _ in range(n)]

flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)