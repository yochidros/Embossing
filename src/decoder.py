import Chipher

def decodeInfo(path):
    is_read = False
    with open(path, 'rb') as f:
        auth_key = f.readline()
        company_id = f.readline()
        email = f.readline()
        password = f.readline()
        is_read = True

    if is_read:
        print(auth_key)
        print(company_id)
        print(email)
        print(password)

