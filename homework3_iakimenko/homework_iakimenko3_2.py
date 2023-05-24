my_str: str = input("Write a sentence:")
# Check if all characters in the string are either letters or spaces
if not all(var.isalpha() or var.isspace() for var in my_str):
    print("Incorrect input.Write only words!")
else:
    # Split the string into words
    word = my_str.split()
    # Count the number of words
    count = len(word)
    # Print count of words
    print("Word(s) number: ", count)

# I tried different options, the task itself is simple.
# But to make it so that there are only letters and a space is a bit difficult.
# I tried many options, maybe I listened to something at a lecture.
# But I had to go to Google.
# If there is an easier way, please let me know.
# As a hint
