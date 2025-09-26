# 3) Datetime Reminder Script
#    - Ask user for a date (YYYY-MM-DD).
#    - Calculate how many days remain until that date.
#    - If it is in the past, print "This date has already passed."
#    - Otherwise, save the reminder into "reminders.txt" in format:
#         "{date} -> {days_left} days left"
#    - Append multiple reminders without overwriting.

from datetime import datetime

def date_reminder():
    date_str = input("enter date in this shape YYYY-MM-DD: ")
    try:
        user_date = datetime.strptime(date_str,"%Y-%m-%d").date()

        today = datetime.today().date()

        if today > user_date:
            print("This date has already passed.")

        else:
            days_left = (user_date - today).days
            with open("reminders.txt", "a") as file:
                file.write(f"{user_date} -> {days_left} days left\n")

    except Exception as e:
            print(f"error : {e}")

# date_reminder()