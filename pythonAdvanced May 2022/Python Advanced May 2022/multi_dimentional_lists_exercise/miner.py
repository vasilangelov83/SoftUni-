from collections import deque


def is_inside(matix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matix)


n = int(input())
commands = deque(input().split())
matrix = []
coal = 0

for _ in range(n):
    x = input().split()
    matrix.append(x)
    for ch in x:
        if ch == "c":
            coal += 1
condition = False

while not condition:
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "s":
                if len(commands) == 0 and coal != 0:
                    print(f"{coal} pieces of coal left. ({row}, {col})")
                    condition = True
                    break
                elif coal == 0:
                    print(f"You collected all coal! ({row}, {col})")
                    condition = True
                    break

                if commands[0] == "left":
                    if is_inside(matrix, row, col - 1):
                        if matrix[row][col - 1] == "e":
                            print(f"Game over! ({row}, {col-1})")
                            condition = True
                        elif matrix[row][col - 1] == "c":
                            coal -= 1
                            matrix[row][col - 1] = "s"
                            matrix[row][col] = "*"

                        else:
                            matrix[row][col - 1] = "s"
                            matrix[row][col] = "*"

                elif commands[0] == "right":
                    if is_inside(matrix, row, col + 1):
                        if matrix[row][col + 1] == "e":
                            print(f"Game over! ({row}, {col + 1})")
                            condition = True
                        elif matrix[row][col + 1] == "c":
                            coal -= 1
                            matrix[row][col + 1] = "s"
                            matrix[row][col] = "*"

                        else:
                            matrix[row][col + 1] = "s"
                            matrix[row][col] = "*"

                elif commands[0] == "up":
                    if is_inside(matrix, row - 1, col):
                        if matrix[row][col - 1] == "e":
                            print(f"Game over! ({row - 1 }, {col})")
                            condition = True
                        elif matrix[row - 1][col] == "c":
                            coal -= 1
                            matrix[row - 1][col] = "s"
                            matrix[row][col] = "*"

                        else:
                            matrix[row - 1][col] = "s"
                            matrix[row][col] = "*"

                elif commands[0] == "down":
                    if is_inside(matrix, row + 1, col):
                        if matrix[row + 1][col] == "e":
                            print(f"Game over! ({row + 1}, {col})")
                            condition = True
                        elif matrix[row + 1][col] == "c":
                            coal -= 1
                            matrix[row + 1][col] = "s"
                            matrix[row][col] = "*"

                        else:
                            matrix[row + 1][col] = "s"
                            matrix[row][col] = "*"

                commands.popleft()



