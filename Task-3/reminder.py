"""
Task 3 - Datetime Reminder
- Ask user for a date
- Calculate days left
- Save reminders to reminders.txt
"""

from datetime import date, datetime

def datetime_reminder():
    while True:
        try:
            user_input = input("Enter a date (YYYY-MM-DD): ")
            target = datetime.strptime(user_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid format. Please enter in YYYY-MM-DD.")

    today = date.today()
    if target < today:
        print("This date has already passed.")
    else:
        days_left = (target - today).days
        with open("reminders.txt", "a") as f:
            f.write(f"{target} -> {days_left} days left\n")
        print(f"Reminder saved: {target} -> {days_left} days left")
