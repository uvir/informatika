def find_common_participants(group_1, group_2, splitter=","): # Создание фукнции для поиска общих участников
    list_group_1 = group_1.split(splitter)
    list_group_2 = group_2.split(splitter)
# Разделяем строки на список фамилий

    all_participants = [] # Создаем пустой список для общих участников

    for name in list_group_1: # Перебираем каждую фамилию из первой группы
        if name in list_group_2: # Проверяем наличие той же фамилии во второй группе
            all_participants.append(name) # Если есть, то добавляем в список
    all_participants.sort() # Сортируем список по алфавиту

    return all_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|") # Вызываем функцию
print(result)
