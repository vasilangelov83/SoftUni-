

row_count, column_count = [int(x) for x in input().split(", ")]


matrix = [[int(x) for x in input().split(" ")]for _ in range(row_count)]

result = []
for column_index in range(column_count):
    column_sum = 0
    for row_index in range(row_count):
        column_sum += matrix[row_index][column_index]
    result.append(column_sum)

[print(x) for x in result]