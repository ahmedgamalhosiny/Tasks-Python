
# 7) Decorators Task
#    - Create a decorator called "log_time" that:
#         - Records the execution time of any function.
#         - Saves the function name and runtime into "execution_log.txt".
#    - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
#    - Verify that the log file contains entries after running.

import time

from math_auto import math_automation       
from regex_cleaner import regex_log_cleaner 


def log_time(function):
    def wrapper():
        start = time.time()
        result = function()
        end = time.time()
        runtime = end - start

        with open("execution_log.txt","a") as file:
            file.write(f"function name {function} => runtime {runtime:}\n")
        return result
    
    return wrapper


# math_automation = log_time(math_automation)
# regex_log_cleaner = log_time(regex_log_cleaner)

# math_automation()
# regex_log_cleaner()

