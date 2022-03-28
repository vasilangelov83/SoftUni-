import re
n = int(input())
for i in range(n):
    string = input()
    pattern = r"^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$"

    matches = re.findall(pattern,string)

    if not matches:
        print("Invalid barcode")
    else:
        product_group = ""
        for code in matches:
            for ch in code:
                if ch.isdigit():
                    product_group += ch
        if not product_group:
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")