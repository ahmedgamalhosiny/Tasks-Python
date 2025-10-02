"""
Task 1 - Math Automation
- Ask user for numbers
- Calculate floor, ceil, sqrt, circle area
- Save results to file
"""

import math

def math_automation():
    while True:
        try:
            nums = input("Enter numbers separated by commas: ").split(",")
            nums = [float(n.strip()) for n in nums]
            break
        except ValueError:
            print("Please enter valid numbers separated by commas.")

    with open("math_report.txt", "w") as f:
        for n in nums:
            f.write(f"Number: {n}\n")
            f.write(f"  floor: {math.floor(n)}\n")
            f.write(f"  ceil: {math.ceil(n)}\n")
            f.write(f"  sqrt: {math.sqrt(n)}\n")
            f.write(f"  circle_area: {math.pi * n * n}\n")
            f.write("-" * 30 + "\n")

    print("math_report.txt created.\n")
    with open("math_report.txt", "r") as f:
        print(f.read())
