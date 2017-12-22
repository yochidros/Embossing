import sys
import Chipher
import AuthKey
from getpass import getpass


def createInfo():
    __companyId = input('please input your company ID: ')
    __name = input('please input your email: ')
    __password = getpass('Password: ')

    if __companyId is '' or __name is '' or __password is '':
        print("ERROR: your input data is invalid!!")
        sys.exit(1)

    auth_key = AuthKey.generate_auth_key()
    cipher = Chipher.AESCipher(auth_key)

    _companyId = cipher.encrypt(__companyId)
    _name = cipher.encrypt(__name)
    _password = cipher.encrypt(__password)

    with open('../.kintai_info', 'wb') as f:
        f.write(str.encode(auth_key + '\n'))
        f.write(_companyId)
        f.write(str.encode('\n'))
        f.write(_name)
        f.write(str.encode('\n'))
        f.write(_password)
        print('Encrypt Done Successfuly!!🍻')
