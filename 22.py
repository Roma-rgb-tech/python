# Документация Функции (DOCSTRING)
# DOCSTRING используется для документирования функций, классов, модулей

# Описание функции 
# def mult_by_factor(value, mult=1):
#     """Multiplies number by multiplicator"""
#     return value * mult

# mult_by_factor(5)


# Описание аргументов 
def print_number_info(num):
    """
    Prints num information  
    Args:
        num (int): Integer number

    Returns:
        int: Same number 
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")
        
    return num
    
print_number_info(5)


