# Запрашиваем количество сувениров и безделушек
souvenirs = int(input("Введите количество сувениров: "))
trinkets = int(input("Введите количество безделушек: "))

# Вес сувенира и безделушки в граммах
weight_souvenir = 75
weight_trinket = 112

# Вычисляем общий вес
total_weight = (souvenirs * weight_souvenir) + (trinkets * weight_trinket)

# Выводим результат
print(f"Общий вес посылки: {total_weight} грамм")
