# Cinema cashier

# Create variable with input function to request an age.
age = input("Write your age: ")

# Checking if the entered value is a string.
if age.isalpha():
    print("Incorrect input! Write a number, please. ")

# Checking for spaces or invalid characters in an age string
# .isnumeric found on the internet.
elif ' ' in age or not age.isnumeric():
    print("Incorrect input! Do not use spaces,letters,words or special characters.Write an integer.")
else:
    # Convert age string to integer.
    age = int(age)

    # Homework + a little bit of myself.
    if age == 0:
        print("Incorrect number(Age cannot be 0).")
    elif age <= 6:
        print("Where's your parents? ")
    elif age <= 16:
        print("This is an adult movie!")
    elif age >= 120:
        print("Call the Guinness Book of Records or write your real age.")
    elif age >= 65:
        print("Show your pension certificate, please!")
    elif "7" in str(age):
        print("You will be lucky!")
    else:
        print("Tickets sold out!")
