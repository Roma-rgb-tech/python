# Самая короткая функция
def my_fn():
    pass  # Ключевое слово


print(my_fn())  # None


# Передача Неизменяемых обьектов
def my_fn(a, b):
    a = a + 1
    c = a + b
    return c

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res) # 15
print(num_one) # 10
    

# Передача изменяемых обьектов в функцию
def increase_person_age(person):
    person['age'] += 1
    return person

person_one = {
    'name': 'Bob',
    'age': 17
}

increase_person_age(person_one)
print(person_one['age']) # 18

# Внутри функции не рекомендуется изменять внешние обьекты 