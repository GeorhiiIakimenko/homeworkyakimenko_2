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

    def get_age_word(age):
        if age % 10 == 1 and 11 != age % 100:
            return "рік"
        elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
            return "роки"
        else:
            return "років"

    if age == 0:
        print("Некоректне число (Вік не може бути 0).")
    elif age < 7:
        print(f"Тобі ж {age} {get_age_word(age)}! Де твої батьки?")
    elif age < 16:
        print(f"Тобі лише {age} {get_age_word(age)}, а це фільм для дорослих!")
    elif age > 65:
        print(f"Вам {age} {get_age_word(age)}? Покажіть пенсійне посвідчення!")
    elif "7" in str(age):
        print(f"Вам {age} {get_age_word(age)}, вам пощастить!")
    else:
        print(f"Незважаючи на те, що вам {age} {get_age_word(age)}, білетів всеодно немає!")


cinema_cashier()