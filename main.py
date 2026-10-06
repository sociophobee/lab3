def print_all(data):
    """Виведення всіх записів словника"""
    print("\n--- Список усіх осіб ---")
    if not data:
        print("Словник порожній.")
        return
    
    for key, info in data.items():
        print(f"ID {key}: {info['прізвище']} {info['ім\'я']}, Зріст: {info['зріст']} см, Стать: {info['стать']}")
    print("------------------------\n")


def add_record(data):
    """Додавання нового запису"""
    try:
        new_id = max(data.keys()) + 1 if data else 1
        surname = input("Введіть прізвище: ")
        name = input("Введіть ім'я: ")
        height = int(input("Введіть зріст (у см): "))
        gender = input("Введіть стать (ч/ж): ").lower()
        
        data[new_id] = {'прізвище': surname, 'ім\'я': name, 'зріст': height, 'стать': gender}
        print(f"Запис успішно додано під ID {new_id}!")
    except ValueError:
        print("Помилка! Зріст має бути цілим числом. Спробуйте ще раз.")


def delete_record(data):
    """Видалення запису з обробкою винятків"""
    try:
        key_to_delete = int(input("Введіть ID запису для видалення: "))
        del data[key_to_delete]
        print(f"Запис з ID {key_to_delete} успішно видалено!")
    except ValueError:
        print("Помилка! ID має бути числом.")
    except KeyError:
        print("Помилка! Запису з таким ID не існує.")


def print_sorted_by_keys(data):
    """Перегляд словника за відсортованими ключами"""
    print("\n--- Відсортовані записи (за ID) ---")
    sorted_keys = sorted(data.keys())
    for key in sorted_keys:
        info = data[key]
        print(f"ID {key}: {info['прізвище']} {info['ім\'я']}, Зріст: {info['зріст']} см, Стать: {info['стать']}")
    print("-----------------------------------\n")


def avg_height_men(data):
    """Варіант: Визначення середнього зросту чоловіків (Завдання Тімліда)"""
    men_heights = []
    for info in data.values():
        if info['стать'] == 'ч':
            men_heights.append(info['зріст'])
    
    if men_heights:
        avg = sum(men_heights) / len(men_heights)
        print(f"\n=> Середній зріст чоловіків: {avg:.2f} см\n")
    else:
        print("\n=> У списку немає чоловіків.\n")


# ==========================================
# ФУНКЦІЯ ВІД СТУДЕНТА 1 (Анастасія)
# ==========================================
def find_tallest_person(data):
    """Функція Студента 1: Пошук людини з найбільшим зростом"""
    if not data:
        print("\n=> Словник порожній.\n")
        return
    
    max_height = 0
    tallest_person = None
    
    for info in data.values():
        if info['зріст'] > max_height:
            max_height = info['зріст']
            tallest_person = info
            
    print(f"\n=> Найвища людина: {tallest_person['прізвище']} {tallest_person['ім\'я']}, Зріст: {max_height} см\n")


# ==========================================
# ФУНКЦІЯ ВІД СТУДЕНТА 2(Дмитрій)
# ==========================================
def count_gender(data):
    """Функція Студента 2: Підрахунок кількості чоловіків та жінок"""
    if not data:
        print("\n=> Словник порожній.\n")
        return
    
    men_count = 0
    women_count = 0
    
    for info in data.values():
        if info['стать'] == 'ч':
            men_count += 1
        elif info['стать'] == 'ж':
            women_count += 1
            
    print(f"\n=> Статистика: Чоловіків - {men_count}, Жінок - {women_count}\n")


def main():
    # Початковий словник на 10 осіб
    people = {
        1: {'прізвище': 'Шевченко', 'ім\'я': 'Тарас', 'зріст': 175, 'стать': 'ч'},
        2: {'прізвище': 'Косач', 'ім\'я': 'Лариса', 'зріст': 162, 'стать': 'ж'},
        3: {'прізвище': 'Франко', 'ім\'я': 'Іван', 'зріст': 172, 'стать': 'ч'},
        4: {'прізвище': 'Марко', 'ім\'я': 'Вовчок', 'зріст': 165, 'стать': 'ж'},
        5: {'прізвище': 'Стус', 'ім\'я': 'Василь', 'зріст': 180, 'стать': 'ч'},
        6: {'прізвище': 'Костенко', 'ім\'я': 'Ліна', 'зріст': 168, 'стать': 'ж'},
        7: {'прізвище': 'Грушевський', 'ім\'я': 'Михайло', 'зріст': 178, 'стать': 'ч'},
        8: {'прізвище': 'Теліга', 'ім\'я': 'Олена', 'зріст': 170, 'стать': 'ж'},
        9: {'прізвище': 'Довженко', 'ім\'я': 'Олександр', 'зріст': 182, 'стать': 'ч'},
        10: {'прізвище': 'Крушельницька', 'ім\'я': 'Соломія', 'зріст': 164, 'стать': 'ж'}
    }

    while True:
        print("====== ГОЛОВНЕ МЕНЮ ======")
        print("1. Показати всі записи")
        print("2. Додати запис")
        print("3. Видалити запис")
        print("4. Показати відсортовано за ID")
        print("5. Знайти середній зріст чоловіків (Моє завдання)")
        print("6. Знайти найвищу людину (Студент 1)")
        print("7. Підрахувати чоловіків та жінок (Студент 2)")
        print("8. Вийти")
        print("==========================")
        
        choice = input("Оберіть дію (1-8): ")
        
        if choice == '1':
            print_all(people)
        elif choice == '2':
            add_record(people)
        elif choice == '3':
            delete_record(people)
        elif choice == '4':
            print_sorted_by_keys(people)
        elif choice == '5':
            avg_height_men(people)
        elif choice == '6':
            find_tallest_person(people)
        elif choice == '7':
            count_gender(people)
        elif choice == '8':
            print("Роботу завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()