# 6) Random Data Generator
#    - Ask user how many random numbers to generate.
#    - Save them into "random_numbers.csv" as:
#         index,value
#         1, 42
#         2, 87
#         ...
#    - Print total count and average of the generated numbers.

import random

def random_int(num , low = -1_000_000, high = 1_000_000):
    for _ in range(num):
        yield random.randint(low, high)

def gen_data():

    try:

        total = 0
        total_sum = 0

        num = int(input("how many random numbers to generate: "))

        
        with open("random_numbers.csv", "w") as file:
            
            file.write("index,value\n")
            
            for i, n in enumerate(random_int(num) , start=1):

                file.write(f"{i},{n}\n")
                total += 1 
                total_sum += n
        avg = total_sum / total 
        print(f"total number generated is : {total}")

        print(f"average value : {avg}")

    except Exception as e:
        print(f"error : {e}")


# gen_data()