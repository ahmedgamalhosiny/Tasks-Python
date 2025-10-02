"""
Task 2 - Regex Log Cleaner
- Create fake access.log
- Extract valid emails
- Save to valid_emails.txt
"""

import re

def regex_log_cleaner():
    fake_logs = [
        "user1@example.com",
        "hello world",
        "admin@test.org",
        "invalid@",
        "contact@domain.com",
        "just text",
        "x@y.z",
        "support@company.net",
        "fake@@mail.com",
        "team@workplace.co"
    ]

    with open("access.log", "w") as f:
        for line in fake_logs:
            f.write(line + "\n")

    with open("access.log", "r") as f:
        content = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)
    unique_emails = set(emails)

    with open("valid_emails.txt", "w") as f:
        for email in unique_emails:
            f.write(email + "\n")

    print(f"Found {len(unique_emails)} unique valid emails.")
    print("valid_emails.txt created.")
