"""
Task 6 - Random Data Generator
- Generate random numbers
- Save to CSV
"""

import random

def random_data_generator():
    while True:
        try:
            count = int(input("How many random numbers? "))
            if count <= 0:
                print("Must be greater than zero.")
                continue
            break
        except ValueError:
            print("Enter a valid integer.")

    with open("random_numbers.csv", "w") as f:
        f.write("index,value\n")
        total = 0
        for i in range(1, count + 1):
            num = random.randint(1, 100)
            total += num
            f.write(f"{i},{num}\n")

    avg = total / count
    print(f"Generated {count} numbers. Average = {avg}")
    print("random_numbers.csv created.")
