"""
    Python Practice Tasks
    =====================

    Rules:
        - Everything must be written inside functions.
        - The file should run as a script.
        - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: Pepole with favorite color , .....).
        - The user chooses a number, and the program runs the corresponding function.
        - Each task should only run when chosen from the menu.
        - At ANY stage: if the user enters invalid input, the program must:
              * Show an error message
              * Display what valid input looks like
              * Let the user try again (do not crash or exit)

    Tasks:
    ------
"""

# 1 - Ask the user to enter 5 numbers.
#     Store them, then display them in ascending order and descending order.
def arrange_nums(*args) :
    while True:

        try:
            nums = list(map(int,input("enter 5 numbers pleaes: ").split()))
            
            l = len(nums) 
            
            if l != 5:
                print("enter 5 nums exactly please")
                continue
            
            nums.sort()
            
            print(f"sorted {l} nums: {nums}")
            
            nums.sort(reverse=True)
            
            print(f"reversed {l} nums: {nums}")
            break
        except Exception as e:
            print("error occur: ", e)


# 2 - Write a function that takes two numbers: (length, start).
#     Generate a sequence of numbers with the given length,
#     starting from the given start number and increasing by one each time.
#     Print the result.

def gen_list(l , s):
    while True:
        try:

            arr = list()
            
            for i in range(l):
                arr.append(s)
                s = s + 1

            print(f"list is: {arr}")
            break
        
        except Exception as e:
            print(f"error occur: {e}")
        

# 3 - Keep asking the user for numbers until they type "done".
#     When finished, print:
#         * The total of all numbers entered
#         * The count of valid entries
#         * The average
#     If the user enters something invalid, show an error and continue.
    
def calc():

    arr2 = list()
    count = 0

    while True:
        try:
            
            num = input("enter integer value please or enter done to exit")
            
            if num == "done":
                break
            
            num = int(num)
            arr2.append(num)
            
        except Exception as e:
            count += 1
            print(f"eror : {e}")
    
    total = sum(arr2)
    l = len(arr2)
    average = total / l

    print(f" total is {total} and average is {average} and num of invalid try is {count}")



# 4 - Ask the user to enter a list of numbers.
#     Remove any duplicates, sort the result, and display it.

def make_set():
    while True:
        try:
            nums = list(map(int , input("enter list of numbers pleae").split()))

            nums = set(nums)

            nums = sorted(nums)


            print(f"after deleting dup and sorting the numbers is {nums}")
            break

        except Exception as e:
            print(f"error {e}")





# 6 - Ask the user to enter a sentence.
#     Count how many times each word appears in the sentence
#     and display the result.

def counter():
    try:

        sentence = input("enter sentence: ")

        words = sentence.split()
        words = set(words)

        for i in words:
            c = sentence.count(i)
            print(f" '{i}' showed {c} times in sentence")

    except Exception as e:
        print(f"error {e}")



# 7 - Create a small gradebook system:
#     - The user enters 5 students names and their scores.
#     - At the end, show:
#         * The highest score
#         * The lowest score
#         * The average score.

def gradebook():
    try:
        student = dict()
        for i in range(5):
            name , score = input("enter your name and score in this shape=> ahmed 50 for 5 students: ").split()
            score = int(score)
            student[name] = score
        
        max_value = max(student.values())
        min_value = min(student.values())
        avg_value = sum(student.values()) / len(student)

        print(f" the max is {max_value} and the min is {min_value} and the average is {avg_value}")

    except Exception as e:
        print(f"error {e}")
        




# 8 - Write a program that simulates a shopping cart:
#     - The user can add items with a name and a price.
#     - The user can remove items by name.
#     - The user can view all items with their prices.
#     - At the end, display the total cost.

def cart():
    cart = dict()

    while True:
            
        try:
            choice = int(input(" enter 1 to add items or 2 to delete itmes or 3 to view all items or 4 to quit "))

            if choice == 1 :
                k , v = input("enter the name of item and the price in this shap : cat 50 ").split()
                cart[k] = int(v)

            elif choice == 2:
                k = input("enter the name of item you want to delete ")
                del cart[k]

            elif choice == 3:
                print(f"your cart content is {cart}")
            
            elif choice == 4:
                break

            total = sum(cart.values())
            print(f"your total cost is {total}")

        except Exception as e:
            print(f"error {e}")
        


# 9 - Create a number guessing game:
#     - The program randomly selects a number between 1 and 20.
#     - The user keeps guessing until they get it right.
#     - After each guess, show if the guess was too high or too low.
#     - When correct, display the number of attempts.
import random

def guess():
    choice = random.randint(1,20)
    count = 0
    while True:
        try:
            
            num = int(input("enter number between 1 and 20: "))

            if num > choice:
                print("too high")
                count += 1

            elif num < choice:
                print("too low")
                count += 1
            else:
                print(f"you got it after {count} times")
                break

        except Exception as e:
            print(f"error {e}")


def menu():
    while True:
        print("\n=== Python Practice Tasks Menu ===")
        print("1: Arrange 5 numbers")
        print("2: Generate a sequence of numbers")
        print("3: Sum & average until 'done'")
        print("4: Remove duplicates & sort a list")
        print("6: Count words in a sentence")
        print("7: Gradebook")
        print("8: Shopping cart")
        print("9: Number guessing game")
        print("0: Exit")

        choice = input("Enter task number: ")

        if choice == "1":
            arrange_nums()
        elif choice == "2":
            l = int(input("Length: "))
            s = int(input("Start: "))
            gen_list(l, s)
        elif choice == "3":
            calc()
        elif choice == "4":
            make_set()
        elif choice == "6":
            counter()
        elif choice == "7":
            gradebook()
        elif choice == "8":
            cart()
        elif choice == "9":
            guess()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Enter a number from 0 to 9.")

# if __name__ == "__main__":
menu()


