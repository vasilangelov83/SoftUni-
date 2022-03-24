import re
n = int(input())
for i in range(n):
    string = input()
    pattern = r"@#+([A-Za-z0-9]{6,})@#+"

    matches = re.findall(pattern,string)

    if not matches:
        print("Invalid barcode")
    else:
        product_code = ""
        for code in matches:
            for ch in code:
                if ch.isdigit():
                    product_code += ch
        if not product_code:
            print("Product group: 00")
        else:
            print(f"Product group: {product_code}")