values = [float(x) for x in input().split()]
occurrences = dict()
for value in values:
    if value not in occurrences.keys():
        occurrences[value] = 1

    else:
        occurrences[value] += 1
for value, count in occurrences.items():
    print(f"{value:.1f} - {count} times")