from math_auto import math_automation
from regex_cleaner import regex_log_cleaner
from reminder import date_reminder
from data_generator import gen_data
from data_transformer import transformer
from file_manager import file_managing
from log import log_time

tasks = {
    1: ("Math Automation", log_time(math_automation)),
    2: ("Regex Log Cleaner", log_time(regex_log_cleaner)),
    3: ("Datetime Reminder", date_reminder),
    4: ("Random Data Generator", gen_data),
    5: ("Product Data Transformer", transformer),
    6: ("OS File Manager", file_managing)
}

def main():
    while True:
        print("\nAvailable Tasks:")
        for num, (name, _) in tasks.items():
            print(f"{num}: {name}")

        choice = input("Enter task number to execute (or 'q' to quit): ").strip()
        if choice.lower() == 'q':
            break
        if not choice.isdigit() or int(choice) not in tasks:
            print("Invalid selection. Try again.")
            continue

        task_func = tasks[int(choice)][1]
        task_func()

if __name__ == "__main__":
    main()
