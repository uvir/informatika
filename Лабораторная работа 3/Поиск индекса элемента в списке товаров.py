def find_index(items, item): # Создаем функцию
    for i in range(len(items)): # Используем цикл для проверки индексов списка
        if items[i] == item: # Проверяем элементы списка на равенство искомому товару
            return i
        
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']: # Перебираем товары
    index_item = find_index(items_list, find_item)

    if index_item is not None: # Если результат не None, выводит индекс
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else: # Если результат None, выводит, что товар не найден
        print(f"Товар '{find_item}' не найден в списке.")
