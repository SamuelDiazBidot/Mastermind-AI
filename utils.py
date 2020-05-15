import re
import time


# Clase que se utiliza para guardar varias funciones que se utilizan en varias partes del programa

validate_numbers = re.compile(r'[1-6]{4}')


# Se utiliza para validar entrada de codigos para el juego de mastermind
def validate(code, length):
        if not code.isdigit():
            print('Code cannot contain other characters other than digits')
            return False
        elif len(code) > length or len(code) < length:
            print('Invalid code length')
            return False
        elif not validate_numbers.fullmatch(code):
            print('Valid numbers are from 1-6')
            return False
        else:
            return True

# Se utiliza para crea una lista con todas las posibilidades de los codigos para el juego de mastermind
def create_mm_codes():
    allowed = re.compile(r'[1-6]{4}')
    n_list = []
    numb = 1111
    while True:
        if allowed.fullmatch(str(numb)):
            n_list.append(str(numb))
        numb += 1
        if len(n_list) == 1296:
            break    
    return n_list

# Se utiliza para validar la entrada de datos, fucnion generica que facilita verificar el resultado
def validate_input(regex, msg_prompt):
    some_regex = re.compile(regex)
    while True:
        usr_in = input(msg_prompt)
        if some_regex.fullmatch(usr_in):
            return usr_in
        else:
            print('Invalid input, try again.')

