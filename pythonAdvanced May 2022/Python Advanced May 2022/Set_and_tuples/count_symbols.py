

string = input()

list_of_chars = []
dict_of_chars_occurrences = {}
for char in string:
    list_of_chars.append(char)
for char in sorted(list_of_chars):
    dict_of_chars_occurrences[char] = list_of_chars.count(char)

for character, occurrence in dict_of_chars_occurrences.items():
    print(f"{character}: {occurrence} time/s")
