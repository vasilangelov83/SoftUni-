

numbers = input().split(" ")
text = input()

index = 0
word = ""
counter = 0
for seq in numbers:
    for num in seq:
        index += int(num)
    index += counter
    if index > len(text):
        word += text[index-len(text)]
        text = text[:index-len(text)] + text[index-len(text):]
    else:
        word += text[index]
        text = text[:index] + text[index:]
    index = 0
    counter += 1
print(word)