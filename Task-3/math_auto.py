
# Rules:
#     1. Every user input must be validated.
#        - If invalid, print error and ask again until valid.
#     2. Each task must be implemented in a separate .py file.
#        - Each file must contain a function that executes the task.
#     3. A main.py file must import all task modules.
#     4. When main.py runs:
#          - Display a menu showing all tasks with their number & name.
#          - Let the user select which task to execute by entering the task number.
#          - Run only the selected task.
#     5. Use if __name__ == "__main__": script only run in main.py`.
#     6. Use functions and avoid code duplication.
#     7. Add comments explaining each step.
#     8. Automate as much as possible (e.g., file creation, processing).
#     9. No hardcoding results.
#     10. Decorators (Task 7) must be applied to at least two tasks.


# 1) Math Automation
#    - Create a file called "math_report.txt".
#    - Ask the user for multiple numbers (comma-separated).
#    - For each number, calculate:
#         - floor, ceil, square root, area of a circle
#    - Write the results into "math_report.txt".
#    - Confirm file was created and print its content.

import math

def math_automation():

   
         try:
            with open("math_report.txt", "w") as file:
               # nums = list(map(float,input("enter multiple nums separated by ',' : ").split(",")))
               nums = [float(x) for x in input("enter multiple nums separated by ',' : ").split(",")]
               for i in nums:
                  fl = math.floor(i)
                  ce = math.ceil(i)
                  sq = math.sqrt(i)
                  cir = math.pi * (i**2)
                  file.write(f"data related to num {i} : the floor is {fl} and ceil is {ce} and square root is {sq} and finally the area of circle is {cir}\n")
            
            with open("math_report.txt", "r") as file:
               output =file.read()
               print(f"the file content\n is {output}")

         except ValueError:
            print("enter valid number please")
            
         except Exception as e:
            print(f"error : {e}")
         

# math_automation()


