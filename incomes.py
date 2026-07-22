def add_incomes():

    name = input("Источник дохода: ").strip()
    while True:
        try:
            amount = float(input("Сколько заработано: "))

            if amount < 0:
                print("Вводите положительные числа!")
                continue

            break

        except ValueError:
            print("Вводите число!")


    income = {
        "type": "incomes",
        "name": name,
        "amount": amount,
        }

    return income
