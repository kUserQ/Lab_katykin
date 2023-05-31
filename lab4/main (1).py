while True:
#Запит шляху до файлу
    file_path = input("Введіть шлях до файлу: ")

    try:
        with open(file_path, 'r') as file:
            total_lines = 0
            empty_lines = 0
            z_lines = 0
            z_count = 0
            and_lines = 0

#Цикл на розпізнавання рядків
            for line in file:
                total_lines += 1
                if line.strip() == '':
                    empty_lines += 1
                if 'z' in line:
                    z_lines += 1
                    z_count += line.count('z')
                if 'and' in line:
                    and_lines += 1
#Вивід результатів
            print(f"Кількість рядків: {total_lines}")
            print(f"Кількість порожніх рядків: {empty_lines}")
            print(f"Кількість рядків з літерою 'z': {z_lines}")
            print(f"Кількість літер 'z' у файлі: {z_count}")
            print(f"Кількість рядків з групою символів 'and': {and_lines}")
#Якщо файлу немає
    except FileNotFoundError:
        print("Файл не знайдено.")
#Кінцева умова зупинки коли захоче користувач
    choice = input("Чи бажаєте продовжити? (так / ні): ")
    if choice.lower() != 'так':
        break
