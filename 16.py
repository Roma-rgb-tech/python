# Как избежать изменения внешних обьектов в функции 
# Внутри функции не рекомендуется изменять внешние обьекты - Это
# можно создать с помощью создание копии обьекта

def increase_person_age(person):
    person_copy = person.copy()
    person_copy['age'] += 1
    return person_copy

person_one = {
    'name': 'Roma',
    'age': 17
}

new_person = increase_person_age(person_one)
print(new_person['age']) # 18
print(person_one['age']) # 17

# Задача функции 
# 1.Создайте функцию merge_list_to_dict
# 2.У функции должно быть два параметра  
# 3.Функция должна обьединять два списка, используя встроенную функцию zip
# 4.Конвертируйте обьект zip в словарь и верните его из функции 
# 5.Вызовите функцию, передав ей два списка в качестве аргументов 
# Выведите результат вызова функции в терминал 

def merge_list_to_dict(list_one, list_two):
   zipped_seq = zip(list_one, list_two)
   return dict(zipped_seq)

res_one = merge_list_to_dict(['a', 'b', 'c' ], [10, True, []])
print(res_one)

res_two = merge_list_to_dict(['abc'], [{}, True, 100])
print(res_two)

res_three = merge_list_to_dict([10, True, 100], ['abc'])
print(res_three)