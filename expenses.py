def add_expense(selected_category):

    print(f"Выбранная категория {selected_category}")
    confirmation = input("Введите + если все верно или - если ошиблись.\nПоле ввода: ")
    
    if confirmation == "+":
        

        name = input("На что была совершена трата: ").strip()
        while True:
            try:
                amount = float(input("Сколько было потрачено(Без -): "))

                if amount < 0:
                    print("Вводите положительные числа!")
                    continue

                break

            except ValueError:
                print("Вводите число!")


        expense = {
            "type": "expenses",
            "name": name,
            "amount": amount,
            "category": selected_category
        }

        return expense
    elif confirmation == "-":
        return
    else:
        print("Неверный ввод!")


def total_expenses(data):
    total = 0
    for expense in data:
        total += expense["amount"]

    return total

def category():
    print("Доступные категории:")
    categories = ["Еда", "Транспорт", "Развлечения", "Подписки", "Здоровье", "Техника", "Прочее"]
    try:
        print("1. Еда\n2. Транспорт\n3. Развлечения\n4. Подписки\n5. Здоровье\n6. Техника\n7. Прочее")
        category_num = int(input("Поле ввода: "))

        if category_num < 1 or 7 < category_num:
            print("Такой категории нет!")
        else:
            return categories[category_num - 1]

    except ValueError:
        print("Вводите номер категории!")


