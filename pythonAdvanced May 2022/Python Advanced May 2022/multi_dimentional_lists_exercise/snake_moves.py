

rows, cols = [int(x) for x in input().split()]

word = input()
index = 0
for row in range(rows):
    line = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols -1, -1, -1)
    for col in range(0, cols, 1):
        line[col] = word[index % len(word)]
        index += 1
    print(''.join(line))