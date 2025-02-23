# Запрос суммы счета у гостя
bill_amount = int(input("Напишите общую сумму счета? "))

# Формула налога от суммы счета (12%)
tax = int(bill_amount * 0.12)

# Формула чаевых от суммы счета (15%)
tip_amount = int(bill_amount * 0.15)

# Вывод результатов
print(f'Общая сумма счета: {bill_amount} soʻm')
print(f'Сумма налога: {tax} soʻm')
print(f'Сумма чаевых: {tip_amount} soʻm')





