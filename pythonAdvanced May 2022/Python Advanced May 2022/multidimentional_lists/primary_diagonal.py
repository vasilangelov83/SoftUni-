

n = int(input())

matrix = [[int(x) for x in input().split(" ")]for _ in range(n)]
result = 0
for row in range(n):
    result += matrix[row][row]
print(result)