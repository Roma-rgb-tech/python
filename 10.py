# Диапазоны (Range)
# Диапазон - Упорядоченная неизменяемая последовательность єлементов
# Диапазоны обычно используеться в циклах

# Структура и синтаксис
my_range = range(5)

print(type(my_range))  # <class 'range'>

print(my_range)  # range(0, 5)

print(list(my_range))  # [0, 1, 2, 3, 4]

# Добавление шага в диапазонах
my_range = range(10, 20, 3)

print(type(my_range))  # <class 'range'>

print(my_range)  # range(10, 20, 3)

print(list(my_range))  # [10, 13, 16, 19]

# Индексы элементов в диапазонах
my_range = range(10, 20, 3)
print(my_range[0])  # 10
print(my_range[1])  # 13
print(my_range[2])  # 16
print(my_range[3])  # 19
print(my_range[4])  # IndexError: range object index out of range

# Использование диапазонов в циклах
my_range = range(10, 20, 3)

for n in my_range:
    print(n)
    # 10
    # 13
    # 16
    # 19

# Практика - Диапазоны
my_range = range(5)

print(my_range)  # range(0, 5)
print(type(my_range))  # <class 'range'>
print(my_range[-1])  # 4

for n in my_range:
    print(n)
    # 0
    # 1
    # 2
    # 3
    # 4
print(my_range[0])

# можно создовать екземпляр range непосредственно в цикле
for n in range(7):
    print(n)
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6


#
for n in range(12, 25, 5):
    print(n)
    # 12
    # 17
    # 22

# Конвертация
print(list(range(12, 25, 5)))  # [12, 17, 22]
print(tuple(range(12, 25, 5)))  # (12, 17, 22)
print(set(range(12, 25, 5)))  # {17, 12, 22}

#
my_range = range(5)

print(dir(my_range))
print(my_range.start)  # 0
print(my_range.stop)  # 5
print(my_range.step)  # 1


#
my_range = range(10, 30, 3)

print(my_range.index(19))  # 3
print(my_range.count(30))  # 0


# Практика - Диапазоны
my_range = range(0, 20, 5)

print(list(my_range))  # [0, 5, 10, 15]
for n in my_range:
    print(n)
