# Аргументы Функций

# Аргументы и параметры функции
def my_fn(a, b):    # (a, b) - Параметры 
    a = a + 1
    c = a + b
    return c

my_fn(10, 3)      # (10, 3) - Аргументы


# Ошибка отсутствия аргументов 
def sum_nums(a, b):
    c = a + b
    return(c)

# Порядок следование аргументов важен - Позиционные аргументы 
print(sum_nums(2, 5)) # 7

print(sum_nums(2)) # TypeError: sum_nums() missing 1 required positional argument: 'b'

print(sum_nums()) # TypeError: sum_nums() missing 2 required positional arguments: 'a' and 'b'



# Ошибка чрезмерного количества аргументов
def sum_nums(a, b):
    c = a + b
    return(c)

print(sum_nums(2, 3, 5)) # TypeError: sum_nums() takes 2 positional arguments but 3 were given




# Обьединение всех аргументов в кортеж функции 
# Может ли функция принимать любое количество аргументов ? - Да

# Обьединение аргументов в Tuple
def sum_nums(*args):
    print(args) # (2, 3, 7)
    print(type(args)) # <class 'tuple'>
    
    print(args[0]) # 2
    return sum(args)

print(sum_nums(2, 3, 7)) # 12
    