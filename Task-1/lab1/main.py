# Lab:
import math

# 	- write a program that prints hello world

print("hello world!")

# 	- application to take a number in binary form from the user, and print it as a decimal

def casting_bin_dec() -> int:
    while True:
        try:
            x = input("enter binary number or enter 'q' to exit: ")
            
            if len(x) == 0:
                print("enter bin number please")
                continue

            if x == 'q':
                break
            
            found=False

            for c in x:
                if c not in ['0','1'] :
                    print("enter binary number please")
                    found=True
                    break

            if found:
                continue

            res = int( x , 2)
            
            print(f"the num in decimal is: {res}")

        except Exception as e:
           print("error: ", e)


casting_bin_dec()



# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"

def divide() -> str:
    while True:
        try:
            x = input("enter number please or 'q' to exit: ")
            if x == 'q':
                break
            if len(x) == 0:
                print("enter number please")
                continue

            x = int(x)

            if not isinstance(x,int):
                print("enter valid number")
                continue

            if x % 3 == 0 and x % 5 ==0:
                print("FizzBuzz")
            
            elif x % 3 == 0:
                print("Fizz")
            
            elif x % 5 ==0:
                print("Buzz")
            
            else:
                print("neither")
        except Exception as e:
            print("error: ", e)

a = divide()


# 	- Ask the user to enter the radius of a circle print its calculated area and circumference



while True:
    try:
        r = input("enter the radius please or q to exit")
        if r == 'q':
            break
        if len(r) == 0:
            print("enter number")
            continue
        
        r = int(r)

        if not isinstance(r, int):
            print("enter valid int value")
            continue
        

        area = math.pi * (r**2)
        circum = 2 * math.pi * r
        print(area)
        print(circum)

    except Exception as e:
            print("error: ", e)       



# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

while True:
    try:
        name = input("enter your name or 'q' to exit: ")
        if name == 'q':
            break

        if len(name.strip()) == 0:
            print("enter a valid name (not empty)")
            continue

        if name.isdigit(): 
            print("name cannot be just numbers")
            continue
        
        email = input("enter your email: ")

        if '@' not in email:
            print("enter a valid email")
            continue

        print(f"hello {name} your email is {email}")

    except Exception as e:
        print("error:", e)



# 	- Write a program that prints the number of times the substring 'iti' occurs in a string 

while True:
    try:
        test = input("Enter a string containing 'iti' (or 'q' to quit): ")

        if test == 'q':
            break

        if len(test.strip()) == 0:
            print("Please enter a non-empty string")
            continue

        if test.isdigit():
            print("String cannot be only numbers")
            continue

        res = test.count("iti")
        print(f"'iti' occurs {res} times in the string")
        break
    except Exception as e:
         print("error:", e)

        





