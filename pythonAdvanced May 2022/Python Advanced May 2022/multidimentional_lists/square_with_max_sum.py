
rows, columns = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]

max_sum = 0
elements = []
for row in range(rows-1):
    for col in range(columns -1):

        current_sum = matrix[row][col+1] + matrix[row+1][col] + matrix[row+1][col+1] + matrix[row][col]
        if max_sum < current_sum:
            max_sum = current_sum
            elements = [matrix[row][col],matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]]

print(f"{elements[0]} {elements[1]}")
print(f"{elements[2]} {elements[3]}")
print(max_sum)
