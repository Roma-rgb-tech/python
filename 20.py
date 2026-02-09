#       Колбэк функции 

def other_fn():
    # some actions...
    pass


def fn_with_callback(callback_fn):           # В теле етой функции вызывается колбэк функция 
    callback_fn()
    
    
fn_with_callback(other_fn)


# Пример 1:

def print_number_info(num):
    if (num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")
        
        
def process_number(num, callback_fn):
    callback_fn(num)
    
def print_square_num(num):
    print("Square of the num is", num * num)
    
    
entered_num = int(input('Enter any number: '))

process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)







# Пример 2:

def send_data(data):
    # sending data to the remote server
    pass

def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()
    # actions with updated_data
    send_data_fn(updated_data)
    
process_data({'name': 'Roman'}, send_data)
