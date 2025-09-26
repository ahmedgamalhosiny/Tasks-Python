# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.

import re
def regex_log_cleaner():
    try:
        with open("access.log", "w") as file:
            file.write("ali@a.com\nahmed@ga.com\nali@al\nahd\najfdkjdkl\n154652@2\nhassan@gmial.com\naaa\n15456\n@##$@4\nahmed44@gmail.com\n")
        
        with open("access.log", "r") as file:
            lines = file.readlines()

            new_lines = list()

            for line in lines:
                if bool(re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",line.strip())):
                    new_lines.append(line)
        
        
        with open("valid_emails.txt" , "w") as file:
            for line in new_lines:
                file.write(f"{line}")

        print(f"{len(new_lines)} valid emails found")
    
    except Exception as e:
            print(f"error : {e}")


# regex_log_cleaner()
