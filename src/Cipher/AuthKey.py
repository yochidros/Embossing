import string
import random
import os

def generate_auth_key():
    _digits_alphabet = string.ascii_letters + string.digits
    _array_str = [random.choice(_digits_alphabet) for _ in range(32)]
    _auth_key = ''.join(_array_str)
    return _auth_key.encode()



