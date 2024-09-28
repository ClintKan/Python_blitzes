#Script that multiplies 2 on every number from 0 to 9

#Intro
print("This script multiplies 2 on every number from 0-9 while printing the answer.\n")

#Finding the proper range for 0-9; range(?)
for number in range(10): # or range (0,10) or range(0,10,1)
    print(f"{number} * 2 = {number * 2}\n")