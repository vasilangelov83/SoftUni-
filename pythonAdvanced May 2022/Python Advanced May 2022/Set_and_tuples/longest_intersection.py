
number_of_lines = int(input())

ranges = [input().split("-") for _ in range(number_of_lines)]

longest_len = 0
longest_intersection = set()
print(longest_intersection)
longest_intersection_formatted = [str(x) for x in longest_intersection]
print(longest_intersection_formatted)
for range_element in ranges:

    start1, stop1 = range_element[0].split(",")
    start2, stop2 = range_element[1].split(",")
    first_set = set(range(int(start1), int(stop1)+1))
    second_set = set(range(int(start2), int(stop2)+1))
    intersection = first_set.intersection(second_set)
    print(intersection)
    if len(intersection) > longest_len:
        longest_len = len(intersection)
        longest_intersection = intersection
print(f"Longest intersection is [[{''.join(longest_intersection_formatted)}]] with length {longest_len}")
