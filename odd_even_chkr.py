#A script checking if the input number is odd or even

#Intro
print("This scripts checks if a number, that's been input, is odd or even")

usr_input = int(input("What number would you like to check?\n"))

numbr_rmdr = usr_input % 2

if numbr_rmdr == 0:
    print(f"The number {usr_input} is even")
else:
    print(f"The number {usr_input} is odd")
    