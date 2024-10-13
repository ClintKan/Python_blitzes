#A script converting teperature from fahrenheit to celsius

print("This is a script to convert temperature; °F => °C")

usr_inpt = float(input("Enter temperature in Fahrenheit: "))

while usr_inpt < 32 or usr_inpt > 212:
    print("Out of range input °F should be between 32°-212°")

    usr_inpt = float(input("Enter temperature in Fahrenheit: "))

celc_temp = round(((usr_inpt - 32) * 5/9), 2)
print(f"{usr_inpt} Fahrenheit is {celc_temp} Celsius")


