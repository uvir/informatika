import json

def task() -> float: # Создаем функцию, которая возвращает число типа float
    with open('input.json','r') as f: # Открываем файл в режим чтения
        data = json.load(f) # Преобрузует его в Python-объект

    sum = 0 # Создаем переменную суммы

    for item in data: # Создвем цикл, проходящий по каждому элементу списка data
        score = item["score"]
        weight = item["weight"]
        sum+=score*weight # Вычисляем сумму

    return round(sum,3)
print(task())
