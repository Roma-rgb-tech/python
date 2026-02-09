# Значения параметров функции по умолчанию
# Пример 1:
def mult_by_factor(value, multiplier=1):
    return value * multiplier

print(mult_by_factor(10, 2)) # 20
print(mult_by_factor(5)) # 5
# Наличие значения по умолчанию для параметра функции делает его необязательным 

# Пример 2:
from datetime import date

def get_weekday():
    return date.today().strftime('%A')

def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['created_on_weekday'] = weekday
    return post_copy

initial_post = {
    'id': 243,
    'author': 'Roman',
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)  # {'id': 243, 'author': 'Roman', 'created_on_weekday': 'Monday'}
