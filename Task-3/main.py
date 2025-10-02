"""
Main Menu:
- Imports all tasks
- Lets user choose which to run
"""

from math_task import math_automation
from regex_cleaner import regex_log_cleaner
from reminder import datetime_reminder
from products import product_transformer
from file_manager import file_manager
from random_data import random_data_generator
from decorators import log_time

# apply decorator to two tasks
math_automation = log_time(math_automation)
regex_log_cleaner = log_time(regex_log_cleaner)

TASKS = {
    1: ("Math Automation", math_automation),
    2: ("Regex Log Cleaner", regex_log_cleaner),
    3: ("Datetime Reminder", datetime_reminder),
    4: ("Product Transformer", product_transformer),
    5: ("OS File Manager", file_manager),
    6: ("Random Data Generator", random_data_generator),
}

def main():
    while True:
        print("\n--- Task Menu ---")
        for k, v in TASKS.items():
            print(f"{k}. {v[0]}")
        try:
            choice = int(input("Choose task number (0 to exit): "))
            if choice == 0:
                print("Exiting...")
                break
            if choice in TASKS:
                TASKS[choice][1]()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    main()
