
def extract_chars(chars):
    return [char for char in chars]
n = int(input())

matrix = [
    extract_chars(input()) for _ in range(n)
]
special_symbol = input()
coordinates = (0,)
condition = False

for i in range(0, n):
    if not condition:
        for j in range(0, n):
            if matrix[i][j] == special_symbol:
                coordinates = i, j

                condition = True
                break


if condition:
    print(coordinates)
else:
    print(f'{special_symbol} does not occur in the matrix')


