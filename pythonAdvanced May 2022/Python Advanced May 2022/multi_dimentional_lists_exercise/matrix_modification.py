
def is_inside(matix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matix)
rows = int(input())

matrix = [
    [int(x) for x in input().split()] for _ in range(rows)
]

while True:
    command = input().split()
    if command[0] == "END":
        break
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if command[0] == "Add":
        if is_inside(matrix,row,col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        if is_inside(matrix, row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
for x in matrix:
    print(*x)