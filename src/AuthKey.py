import string
import random


def generate_auth_key():
    _digits_alphabet = string.ascii_letters + string.digits
    _array_str = [random.choice(_digits_alphabet) for _ in range(50)]
    _auth_key = ''.join(_array_str)
    return _auth_key
