# Встроенная функция ZIP

# Пример
fruits = ['apple', 'banana', 'lime ']

quantities = [100, 70, 50]

fruit_qtys_zip = zip(fruits, quantities)

print(fruit_qtys_zip)  # <zip object at 0x105679bc0>

print(type(fruit_qtys_zip))  # <class 'zip'>

fruit_qtys_list = list(fruit_qtys_zip)

print(fruit_qtys_list)  # [('apple', 100), ('banana', 70), ('lime ', 50)]

# Пример

names = ['Roman', 'Alex', 'Ivan']
ages = [17, 18, 19]
cities = ['Kiev', 'Lviv', 'Odesa']

print(list(zip(names, ages, cities)))
# [('Roman', 17, 'Kiev'), ('Alex', 18, 'Lviv'), ('Ivan', 19, 'Odesa')]


# Конвертация zip в dict
# При конвертации zip обьекта в словарь допускается только 2 аргумента в вызове функции zip
names = ['Roman', 'Alex', 'Ivan']
ages = [17, 18, 19]

names_ages_zip = zip(names, ages)

print(names_ages_zip)

names_ages_dict = dict(names_ages_zip)

print(names_ages_dict)  # {'Roman': 17, 'Alex': 18, 'Ivan': 19}

# Практика zip

product = ['milk', 'orange', 'bread', 'coke']
price = [20, 5, 15, 2]


product_price_zip = list(zip(product, price))

print(product_price_zip)
# [('milk', 20), ('orange', 5), ('bread', 15), ('coke', 2)]

product_price_dict = dict(product_price_zip)
print(product_price_dict)  # {'milk': 20, 'orange': 5, 'bread': 15, 'coke': 2}
