import re

n = int(input())

for i in range(n):
    input_barcode = input()

    pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

    matches = re.fullmatch(pattern, input_barcode)

    if matches is None:
        print("Invalid barcode")
    else:
        barcode = matches[1]
        product_group = ""
        for ch in barcode:
            if ch.isdigit():
                product_group += ch

        if product_group == "":
            print("Product group: 00")
        else:
            print(f"Product group: {product_group}")
