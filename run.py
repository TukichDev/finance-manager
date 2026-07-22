from actions import actions_print
from expenses import add_expense, total_expenses, category
from loading import load
from storage import load_data, save_data, clear_data, balance
from incomes import add_incomes
import time

selected_category = None

_action = 0
data = load_data()


while _action != 9:
    total_expenses_ = 0
    actions_print()
    try:
        _action = int(input("Поле ввода: "))

        if _action == 1: #Добавление доходов
                    data.append(add_incomes())
                    save_data(data)
                    print("=== Успешно добавлено ===")

        elif _action == 2: #Блок добавления расходов 
            
            if selected_category == None: # Проверка на категорию
                print("=== Сперва выберите категорию! ===")
            else:
                add_expense_ = add_expense(selected_category)

                if add_expense_ is None: #Если пользователь ошибся с категорией
                    continue
                else: #Добавление расходов
                    data.append(add_expense_)
                    save_data(data)
                    print("=== Успешно добавлено ===")
            
        elif _action == 3:  #Сумма расходов
            load() 
            
            for exp in data:
                if exp["type"] == "expenses":
                    total_expenses_ += exp["amount"]
                else:
                    pass

            print(f"=== Сумма расходов: {total_expenses_} ===") 
            
        elif _action == 4:  #
            load()
            if not data:
                print("=== Пока нет операций ! ===")

            else:
                print("=== Операции ===")
                for operations in data:
                    if operations["type"] == "expenses":
                        print(f"Трата | {operations['category']}: {operations['name']} - {operations['amount']} ₽")
                        time.sleep(0.1)
                    else:
                        print(f"Доход: {operations['name']} - {operations['amount']} ₽")
                        time.sleep(0.1)
                        
        elif _action == 5:  #Выбор категории для расходов 
            selected_category = category()
            print("Успешно!")

        elif _action == 6: # очистка Json
            load()
            clear_data()
            data = []
            
        elif _action == 7: #Текущий баланс
            load()
            print(f"==== Текущий баланс: {balance()} ====")

        elif _action == 9: #Выхож
            break
        
        else: #Проверка на верность номера действий
            print('=== Такого действия нет! ===')
            
    except ValueError:
        print("Неверный ввод!")
