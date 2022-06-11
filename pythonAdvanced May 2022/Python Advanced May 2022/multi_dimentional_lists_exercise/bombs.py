def get_children(matrix, row, col):

    possible_children_coordinates = [
        [row-1,col-1],
        [row-1, col],
        [row-1,col +1],
        [row, col -1],
        [row,col+1],
        [row + 1, col - 1],
        [row + 1, col],
        [row+1, col + 1]
    ]
    result = []
    for child_row, child_col in possible_children_coordinates:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result
n = int(input())

matrix = [
    [int(x) for x in input().split()] for _ in range(n)]

bombs = [[int(x) for x in bomb.split(",")] for bomb in input().split() ]
for bomb in bombs:
    row, col = bomb
    power = matrix[row][col]

    if power < 0:
        continue
    matrix[row][col] = 0
    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power
active_cells_count = 0
active_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            active_cells_count += 1
            active_cells_sum += el
print(f'Alive cells: {active_cells_count}')
print(f'Sum: {active_cells_sum}')

for row in matrix:
    print(*row, sep=" ")
