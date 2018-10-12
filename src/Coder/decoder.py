import sys
sys.path.append('../')
from Chipher import Chipher


def decodeInfo(path):
    is_read = False
    with open(path, 'rb') as f:
        auth_key = f.readline()
        company_id = f.readline()
        email = f.readline()
        password = f.readline()
        is_read = True

    if is_read:
        
        auth_key = auth_key.decode()
        auth_key = auth_key[:len(auth_key)]

        chipher = Chipher.AESCipher(auth_key)

        company_id = chipher.decrypt(company_id)
        email = chipher.decrypt(email)
        password = chipher.decrypt(password)

        return [company_id, email, password]
    else:
        print("Error: couldn't find " + path)

def decodeCommonInfo(path):
    is_read = False
    with open(path, 'rb') as f:
        auth_key = f.readline()
        email = f.readline()
        password = f.readline()
        is_read = True

    if is_read:
        
        auth_key = auth_key.decode()
        auth_key = auth_key[:len(auth_key)]

        chipher = Chipher.AESCipher(auth_key)
        email = chipher.decrypt(email)
        password = chipher.decrypt(password)

        return [email, password]
    else:
        print("Error: couldn't find " + path)

