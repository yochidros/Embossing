import sys
sys.path.append('../')
from Cipher.AuthKey import generate_auth_key
from Cipher.Cipher import AESCipher
from getpass import getpass
import os
import base64


def createCommonIdInfo(filename):
    __email = input('please common ID email: ')
    __password = getpass('Password: ')

    if __email is '' or __password is '':
        print("ERROR: your inputed data is invalid!!")
        sys.exit(1)

    #binary
    auth_key = generate_auth_key()
    iv = os.urandom(16)
    cipher = AESCipher(auth_key,iv)
    _email = cipher.encrypt(__email)
    _password = cipher.encrypt(__password)
    iv = base64.b64encode(iv).decode()
    filename = "../" + filename 
    with open(filename, 'wb') as f:
        f.write(str.encode(auth_key.decode() + '\n'))
        f.write(str.encode(iv + '\n'))
        f.write(_email)
        f.write(str.encode('\n'))
        f.write(_password)
        f.write(str.encode('\n'))
        print('Encrypt Done Successfuly!!🍺')
        return True

    return False

if __name__ == '__main__':
    createCommonIdInfo('.test')
