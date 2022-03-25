import re

text = input()
pattern = r"((\:{2})([A-Z][a-z]{2,})(\:{2}))|((\*{2,})([A-Z][a-z]{2,})(\*{2}))"
cool_threshold = 1
for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)

matches = re.finditer(pattern,text)
coolness_dict = {}
emojies = []
for match in matches:
    emoji1 = match.group(1)
    emoji2 = match.group(5)
    word1 = match.group(3)
    word2 = match.group(7)
    if word1 is not None:

        coolness = 0
        for ch in word1:
            coolness += ord(ch)
        coolness_dict[word1] = coolness

    if word2 is not None:

        coolness = 0
        for ch in word2:
            coolness += ord(ch)
        coolness_dict[word2] = coolness
    if emoji1 is not None:
        emojies.append(emoji1)
    else:
        emojies.append(emoji2)
print(f"Cool threshold: {cool_threshold}")
print(f'{len(coolness_dict.keys())} emojis found in the text. The cool ones are:')

for key, value in coolness_dict.items():

    if coolness_dict[key] > cool_threshold:
        for emoji in emojies:
            if key in emoji:
                print(emoji)
