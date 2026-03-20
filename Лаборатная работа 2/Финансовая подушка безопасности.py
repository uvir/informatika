money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0 # Количество месяце, которое можно протянуть без долгов
while True:
    difference=spend-salary # Сколько денег не хватает после зарплаты
    if money_capital<difference: # Проверка, хватает ли подушки
        break

    money_capital=money_capital-difference # Вычитаем из подушки недостоющую сумму
    spend=spend*(1+increase) # Увеличиваем расходы на 5%
    months = months + 1 # Увеличиваем количество прожитых месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months)
