import random


def get_user_choice():
    """
    Отримує вибір користувача: камінь (r), папір (p) або ножиці (s).
    Повертає вибір користувача.
    """
    while True:
        choice = input("Оберіть свій вибір (r - камінь, p - папір, s - ножиці): ").lower()
        if choice in ["r", "p", "s"]:
            return choice
        else:
            print("Некоректний вибір. Будь ласка, спробуйте ще раз.")


def get_computer_choice():
    """
    Генерує випадковий вибір комп'ютера: камінь (r), папір (p) або ножиці (s).
    Повертає вибір комп'ютера.
    """
    choices = ["r", "p", "s"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """
    Визначає переможця гри залежно від вибору користувача і комп'ютера.
    Повертає результат гри: "user" - користувач переміг, "computer" - комп'ютер переміг, "tie" - нічия.
    """
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (
            user_choice == "s" and computer_choice == "p"):
        return "user"
    else:
        return "computer"


def print_result(result, user_choice, computer_choice):
    """
    Виводить на екран результат гри: переможець і їхні вибори.
    """
    if result == "tie":
        print("Нічия!")
    elif result == "user":
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")

    choices = {"r": "камінь", "p": "папір", "s": "ножиці"}
    print(f"Ваш вибір: {choices[user_choice]}")
    print(f"Вибір комп'ютера: {choices[computer_choice]}")


def play_game():
    """
    Функція для гри "Rock paper scissors".
    """
    print("Гра 'Rock paper scissors'")
    print("-------------------------")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print_result(result, user_choice, computer_choice)


play_game()
