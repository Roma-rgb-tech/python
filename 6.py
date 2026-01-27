# Списки List
# Список - Упорядоченная последовательность єлементов
# Порядок єлементов в списке имеет значение
# Структура и синтаксис

posts_ids = [151, 245, 762, 167]
user_inputs = [True, 'hi', '#', 10.5]
print(my_fruits * 2)

my_fruits = ['apple', 'banan', 'lime']
other_fruits = ['banana', 'apple', 'lime']
print(my_fruits == other_fruits)


# Длина списка
empty_list = []
print(len(empty_list))  # 0

my_fruits = ['apple', 'banana', 'lime']
print(len(my_fruits))   # 3

posts_ids = [12, 2, 5, 23]
print(len(posts_ids))  # 4

user_inputs = [True, 'hi']
print(len(user_inputs))  # 2


# Получение значений
posts_ids = [151, 245, 762, 122]

print(posts_ids[1])  # 245
print(posts_ids[2])  # 762
print(posts_ids[-1])  # 122


# Изменение значений
fruits = ['apple', 'pear', 'mango', 'kiwi']

fruits[0] = 'banana'
fruits[3] = 'guava'

print(fruits)  # ['banana', 'pear', 'mango', 'guava']


# Удаление елементов
fruits = ['apple', 'pear', 'mango', 'kiwi']

del fruits[0]
print(fruits)  # ['pear', 'mango', 'kiwi']

del fruits[1]
print(fruits)  # ['pear', 'kiwi']


# Списки , Списки словарей

users = [
    {
        'user_id': 125,
        'user_name': 'Roman'
    },
    {
        'user_id': 52,
        'user_name': 'Eva'
    }
]

print(len(users))  # 2
print(users[1]['user_id'])  # 52


# Списки использование переменных
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]

print(all_fruits)  # ['apple', 'banana', 'lime']


# Списки , Несуществующие єлементы
posts_ids = [152, 52, 34, 43]

print(posts_ids[10])  # IndexError: list index out of range

# Методы Списков
# append, pop, remove, insert, sort,
# index, clear, copy, extend, reverse, count.
# Методы списков обьекты наследуют от класса List

# Списки Append добавление новых элементов в конец списка
fruits = []

fruits.append('Apple')
fruits.append('Banana')
fruits.append('Pear')
fruits.append('Kiwi')

print(fruits)  # ['Apple', 'Banana', 'Pear', 'Kiwi']

print(len(fruits))  # 4

# Списки pop Удаление елементов
fruits = ['Pear', 'Mango', 'Passion fruit', 'Guava']

fruits.pop()
print(fruits)  # ['Pear', 'Mango', 'Passion fruit']

fruits.pop(0)
print(fruits)  # ['Mango', 'Passion fruit']


removed_element = fruits.pop()
# метод pop возвращает тот елемент который был удален
print(removed_element)  # Passion fruit


# Списки sort Сортировка елементов

posts_ids = [4, 2, 1, 3]

posts_ids.sort()

print(posts_ids)  # [1, 2, 3, 4]

posts_ids.sort(reverse=True)

print(posts_ids)  # [4, 3, 2, 1]


# Конвертация в список
greeting = "Hello from Python"
greeting_letters = list(greeting)

# 'H', 'e', 'l', 'l', 'o', ' ', 'f', 'r', 'o', 'm', ' ', 'P', 'y', 't', 'h', 'o', 'n']
print(greeting_letters)

my_dict = {'a': 10, 'b': True}
my_dict_keys = list(my_dict)

print(my_dict_keys)  # ['a', 'b']


# Арифметические операции в списках
ratings = [2.5, 5.0, 4.3, 3.7]

print(min(ratings))  # 2.5
print(max(ratings))  # 5.0
print(sum(ratings))  # 15.5

print(sum(ratings)/len(ratings))  # 3.875


# Списки. Обьединение списков
my_ratings = [2.5, 5.0]

other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)  # [2.5, 5.0, 3.7, 4.5, 4.9]


# Нарезка Списков

ratings = [2.5, 5.0, 4.3, 3.7, 4.5]

first_two_ratings = ratings[:2]
print(first_two_ratings)  # [2.5, 5.0]

middle_ratings = ratings[1:-1]
print(middle_ratings)  # [5.0, 4.3, 3.7]

last_two_ratings = ratings[-2:]
print(last_two_ratings)  # [3.7, 4.5]


# Копирование списка

my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']

print(my_cars)  # ['BMW', 'Mercedes', 'Audi']

print(id(my_cars)) == id(copied_cars)  # True


# Копирование в новый список
# Вариант 1:
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars[:]  # Копирования испоользуя slice

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']

print(my_cars)  # ['BMW', 'Mercedes']

print(id(my_cars) == id(copied_cars))  # False

# Вариант 2:
my_cars = ['BMW', 'Mercedes']

copied_cars = my_cars.copy()

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']

print(my_cars)  # ['BMW', 'Mercedes']

print(id(my_cars) == id(copied_cars))  # False

# Вариант 3:
my_cars = ['BMW', 'Mercedes']

copied_cars = list(my_cars)

copied_cars.append('Audi')

print(copied_cars)  # ['BMW', 'Mercedes', 'Audi']

print(my_cars)  # ['BMW', 'Mercedes']

print(id(my_cars) == id(copied_cars))  # False


#

my_nums = [10, 50, 0, 5, 100, 5]

my_nums.append(25)  # [10, 50, 0, 5, 100, 5, 25]
print(my_nums)


fruit = [1, 'abc', True, 3.4]

del fruit[3]
print(fruit)

fruits = ['Banan', 'apple']

res = fruit + fruits
print(res)
print(len(res))
