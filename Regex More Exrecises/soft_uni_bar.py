import re

info = input()
pattern = r"%([A-Z][a-z]+)%([a-z@*#!&/\`~+=^\-]+)?<(\w+)>([a-z@*#!&/\`~+=^\-]+)?\|(\d+)\|([a-z@*#!&/\`~+=^\\]+)?(-?\d+\.?\d+)\$"
total_income = 0
while info != "end of shift":
    matches = re.finditer(pattern,info)

    for match in matches:
        name = match[1]
        product = match[3]
        count = int(match[5])
        price = float(match[7])
        total_price = price * count
        total_income += total_price
        print(f"{name}: {product} - {total_price:.2f}")
    info = input()
print(f"Total income: {total_income:.2f}")