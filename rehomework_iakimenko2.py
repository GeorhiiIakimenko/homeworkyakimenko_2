age = input("Write your age: ")

if age.isdigit():
    age = int(age)

    if age == 0:
        print("Incorrect number (Age cannot be 0).")
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
else:
    print("Incorrect input! Write a integer number, please.")