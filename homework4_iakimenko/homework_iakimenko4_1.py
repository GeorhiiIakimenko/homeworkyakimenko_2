str1 = input("Write a string: ")
# Checking if the input string contains only letters and spaces
if not all(var.isalpha() or var.isspace() for var in str1):
    print("Incorrect input")
else:
    count = 0
    words = str1.split()

    for word in words:
        vowel_count = 0
        max_vowel_count = 0

        for element in word:
            # Counting the number of vowels in the word
            if element.lower() in "aeiouy":
                vowel_count += 1
                if vowel_count > max_vowel_count:
                    max_vowel_count = vowel_count
            else:
                vowel_count = 0
        # Checking if the word has two or more consecutive vowels
        if max_vowel_count >= 2:
            count += 1

    print("Word(s) number with two or more consecutive vowels: ", count)
