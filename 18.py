# Позиционные аргументы

def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info

info = get_posts_info('Roman', 25)
print(info) # Roman wrote 25 posts



# Аргументы с ключевыми словами 
# Аргументы с ключевыми словами порядок аргументов не важен
def get_posts_info(name, posts_qty):
    info = f"{name} wrote {posts_qty} posts"
    return info

info = get_posts_info(posts_qty=17, name='Roman')
print(info) # Roman wrote 17 posts
# Использование аргументов с ключевыми словами делает код более читабельным 






# Обьединение именованых аргументов в словарь(dict)
def get_posts_info(**person):
    print(person)
    # {'name': 'Roman', 'posts_qty': 25}
    print(type(person)) # <class 'dict'>
    info = (
        f"{person['name']} wrote "
        f"{person['posts_qty']} posts "
    )
    return info

info = get_posts_info(name='Roman', posts_qty=25, id=52)
print(info) # Roman wrote 25 posts


# Задачи - Именованые аргументы функций 

# Задача 1:

# 1.Перепишите вызов функции merge_list_to_dict из предыдущей задачи, так чтобы в нем
# использовались аргументы с ключевыми словами 
# 2. Добавьте еще один вызов функции, в котором будет один позиционный аргумент, а второй-
# аргумент с ключевым словом 
def merge_list_to_dict(list_one, list_two):
    info = f"{list_one} wrote {list_two} book"
    return info

info = merge_list_to_dict(list_one='Roman', list_two=17)
print(info) # Roman wrote 17 book

info = merge_list_to_dict('Roman', list_two=17)
print(info) # Roman wrote 17 book


# Задача 2:
# 1.Создайте функцию update_car_info, в которой все 
# именованные аргументы будут обьединяться в словарь car
# 2. Добавьте в словарь новый ключ is_available с значением True 
# 3.Верните из функции измененный словарь
# 4. Вызовите функцию с именованными аргументами brand и price, их значения могут быть любыми 
# 5. Выведите в терминал результат функции 

def update_car_info(**car):
    car['is_available'] = True
    return car

print(update_car_info(brand='nike', price=10000))
# {'brand': 'nike', 'price': 10000, 'is_available': True}