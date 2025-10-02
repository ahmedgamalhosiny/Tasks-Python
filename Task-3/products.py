"""
Task 4 - Product Data Transformer
- Pair products with prices
- Filter out invalid prices
- Add discounted price
- Save to products.json
"""

import json

def product_transformer():
    while True:
        try:
            names = input("Enter product names (comma-separated): ").split(",")
            prices = [float(x) for x in input("Enter product prices (comma-separated): ").split(",")]
            if len(names) != len(prices):
                print("Names and prices must match in count.")
                continue
            break
        except ValueError:
            print("Please enter valid numbers for prices.")

    pairs = zip(names, prices)
    filtered = filter(lambda p: p[1] > 0, pairs)
    transformed = [{"product": n.strip(), "price": p, "discounted": p * 0.9} for n, p in filtered]

    with open("products.json", "w") as f:
        json.dump(transformed, f, indent=4)

    print("products.json created.")
    print("Preview:", transformed[:5])
