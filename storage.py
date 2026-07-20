import json

file_name = "data.json"


def load_data():
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Файл был поврежден! Начинаем с пустого списка")
        return []

def save_data(data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def clear_data():
    with open('data.json', 'w') as f:
        json.dump([], f)
    