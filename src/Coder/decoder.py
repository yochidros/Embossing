import sys
sys.path.append('../')
from Cipher.Cipher import AESCipher
import base64


def decodeCommonInfo(path):
    is_read = False
    with open(path, 'rb') as f:
        auth_key = f.readline()
        iv = f.readline()
        email = f.readline()
        password = f.readline()
        is_read = True

    if is_read:
        
        auth_key = auth_key.decode()
        auth_key = auth_key[:len(auth_key)]
        iv = iv.decode()
        iv = iv[:len(iv)]
        iv = base64.b64decode(iv)

        chipher = AESCipher(auth_key.encode(), iv)

        email = chipher.decrypt(email)
        password = chipher.decrypt(password)

        return [email, password]
    else:
        print("Error: couldn't find " + path)


if __name__ == '__main__':
   print(decodeCommonInfo('../.test'))
