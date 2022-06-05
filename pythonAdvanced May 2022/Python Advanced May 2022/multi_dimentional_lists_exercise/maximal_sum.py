
rows, cols = [int(x) for x in input().split(' ')]

matrix = [
    [int(x) for x in input().split(" ")] for _ in range(rows)
]
max_sum = float('-inf')
first_cell = (0,)

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +\
                       matrix[row+1][col] + matrix[row+1][col+1]+ matrix[row+1][col + 2] +\
                        matrix[row+2][col] + matrix[row+2][col+1]+ matrix[row+2][col + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            first_cell = row, col
x, y = first_cell
print(f"Sum = {max_sum}")
print(f"{matrix[x][y]} {matrix[x][y + 1]} {matrix[x][y + 2]}")
print(f"{matrix[x+1][y]} {matrix[x+1][y + 1]} {matrix[x+1][y + 2]}")
print(f"{matrix[x+2][y]} {matrix[x+2][y + 1]} {matrix[x+2][y + 2]}")