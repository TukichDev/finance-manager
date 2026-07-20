from actions import actions_print
from expenses import add_expense, total_expenses, category
from loading import load
from storage import load_data, save_data, clear_data
import time

selected_category = None

_action = 0
data = load_data()


while _action != 9:
    actions_print()
    try:
        _action = int(input("Поле ввода: "))
        if _action == 1:
            
            if selected_category == None:
                print("--- Сперва выберите категорию! ---")
            else:
                add_expense_ = add_expense(selected_category)

                if add_expense_ is None:
                    continue
                else:
                    data.append(add_expense_)
                    save_data(data)
                    print("--- Успешно добавлено ---")
            
        elif _action == 2:
            load()
            print(f"--- Сумма расходов: {total_expenses(data)} ---")
            
        elif _action == 3: 
            load()
            if not data:
                print("Пока нет расходов !")

            else:
                print("--- Траты ---")
                for expense_ in data:
                    print(f"{expense_['category']}: {expense_['name']} - {expense_['amount']} ₽")
                    time.sleep(0.1)
                print(f"====================\nИтого: {total_expenses(data)}")

        elif _action == 4:
            selected_category = category()
            load()


        elif _action == 5: # очистка Json
            load()
            clear_data()
            data = []
            

        elif _action == 9:
            break
        
        else:
            print('--- Такого действия нет! ---')
            
    except ValueError:
        print("Неверный ввод!")
