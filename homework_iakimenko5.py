import random
print("Welcome to car brand hangman!")
print("In this game you need to quiz the car brand! Good Luck!")
word_list = ["tesla", "audi", "mercedes", "hyundai", "kia", "bmw", "cadillac", "mitsubishi", "porsche"]

available_letters = 'abcdefghijklmnopqrstuvwxyz'

play_again = True

while play_again:
    # Select a random word from the word list
    word = random.choice(word_list)
    # Create a string of hidden characters to represent the word
    guess_result = '▢' * len(word)
    # List to store the correctly guessed letters
    guessed_letters = []
    # Set to store the entered letters
    entered_letters = set()
    # Number of attempts allowed
    attempts = 5

    while attempts > 0:
        print(f'Guess the word: {guess_result}')
        # Provide hints about the remaining attempts
        if attempts == 3:
            print("You have 3 attempts left!")
        if attempts == 1:
            print("Last attempt!Be careful")
        while True:
            # Prompt the user to enter a letter
            user_letter = input('Enter a letter: ').lower()
            # Validate the user input
            if len(user_letter) != 1:
                print('Please enter a single letter.')
                continue
            elif user_letter not in available_letters:
                print('Invalid input. Please enter a valid letter.')
                continue
            elif user_letter in entered_letters:
                print('You have already guessed that letter. Try again.')
                continue
            # Add the entered letter to the set
            else:
                entered_letters.add(user_letter)
                break

        if user_letter in word:
            guessed_letters.append(user_letter)
            # Update the guess result to reveal the correctly guessed letters
            guess_result = ''.join([char if char in guessed_letters else '▢' for char in word])
        else:
            print('Incorrect guess! Try again.')
            attempts -= 1

        if guess_result == word:
            print(f'Congratulations! You guessed the word.')
            break

    if attempts == 0:
        print('Game over! You have used all your attempts. Good luck next time!')
    print(f"Answer was {word}")
    # Ask the user if they want to play again
    play_again_input = input('Do you want to play again? (Yes/No): ').lower()
    play_again = play_again_input == 'yes'

print('Thank you for playing!')
