import re

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