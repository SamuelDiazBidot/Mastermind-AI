import re
import time

validate_numbers = re.compile(r'[1-6]{4}')

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


def validate_input(regex, msg_prompt):
    some_regex = re.compile(regex)
    while True:
        usr_in = input(msg_prompt)
        if some_regex.fullmatch(usr_in):
            return usr_in
        else:
            print('Invalid input, try again.')

