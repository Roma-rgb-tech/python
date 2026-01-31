# Изменение обьектов в Python
# Переменная содержит ссылку на обьект
# Переменные могут ссылаться на один и тотже обьект в памьяти

# Адреса неизменяемых обьектов
my_number = 10
print(id(my_number))  # 4382975032

other_number = 10
print(id(other_number))  # 4382975032

print(id(10))  # 4382975032

# Копирование неизменяемых обьектов
first_num = 10
second_num = first_num

print(id(first_num))  # 4388938808
print(id(second_num))  # 4388938808

second_num += 5
print(second_num)  # 15
print(first_num)  # 10

print(id(second_num))  # 4392871128
print(id(first_num))  # 4392870968

# Адреса изменяемых обьектов
my_list = [1, 2, 3]
print(id(my_list))
