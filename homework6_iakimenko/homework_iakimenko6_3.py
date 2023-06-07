def get_age_word(age):
    if age % 10 == 1 and age % 100 != 11:
        return "рік"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "роки"
    else:
        return "років"


def cinema_cashier():
    age = input("Введіть свій вік: ")

    if age.isalpha():
        print("Некоректне введення! Будь ласка, введіть число.")
        return

    if ' ' in age or not age.isnumeric():
        print(
            "Некоректне введення! Не використовуйте пробіли, літери, слова або спеціальні символи. Введіть ціле число.")
        return

    age = int(age)
    age_word = get_age_word(age)  # Передайте аргумент 'age' при виклику функції get_age_word

    if age == 0:
        print("Некоректне число (Вік не може бути 0).")
    elif age < 7:
        print(f"Тобі ж {age} {age_word}! Де твої батьки?")
    elif age < 16:
        print(f"Тобі лише {age} {age_word}, а це фільм для дорослих!")
    elif age > 65:
        print(f"Вам {age} {age_word}? Покажіть пенсійне посвідчення!")
    elif "7" in str(age):
        print(f"Вам {age} {age_word}, вам пощастить!")
    else:
        print(f"Незважаючи на те, що вам {age} {age_word}, білетів всеодно немає!")


cinema_cashier()
