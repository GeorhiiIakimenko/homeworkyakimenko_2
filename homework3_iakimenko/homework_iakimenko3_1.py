word = input("Write the word: ")
if word.isalpha():
    index = input("Write symbol's number: ")
    if index.isdigit():
        index = int(index)

        symbol = word[index - 1]  # Index numbers in rows start at 0, we need to enter 1 for the entered number
        result = f"The {index} symbol in {word} is {symbol}"
        print(result)
    else:
        print("Write a number!")
else:
    print("Write the word!")
