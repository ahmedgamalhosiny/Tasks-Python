# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.

import json

def transformer():

    products = [i for i in input("enter product names separated by ',' :").split(",")]
    prices = [float(i) for i in input("enter product prices separated by ',' :").split(",")]

    prod_price = zip(products , prices)

    pos_prod_price = filter(lambda x: x[1] > 0, prod_price)

    new_dicts =  map(lambda x: {"product": x[0], "price":x[1], "discount":x[1]*0.9}, pos_prod_price)

    list_of_dicts = list(new_dicts)

    with open("products.json", "w") as file:
        json.dump(list_of_dicts , file , indent=2)
    print(f"first 5 results is : {list_of_dicts[:5]}")

# transformer()
