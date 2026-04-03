# Имопртируем библиотеки
import csv
import json

# Задаем переменные с именами файлов
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        lines = f.readlines() # Читает весь файл построчно

        headers = lines[0].strip().split(",") # Получаем заголовки
        data=[] # Создаем пустой список для результата

    for line in lines[1:]: # Перебор строк CSV
        values = line.strip().split(",") # Разделение значений строки
        row={} # Создаем словаря строки
        for i in range(len(headers)):
            row[headers[i]]=values[i] # Соединяем заголовки со значениями
        data.append(row) # Добавляем строки в список
    with open(OUTPUT_FILENAME, "w") as f: # Записываем JSON
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f: # Вывод результатов
        for line in output_f:
            print(line, end="")
