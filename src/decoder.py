import Chipher

def decodeInfo(path):
    with open(path, 'rb') as f:
        auth_key = f.readline()
        print(auth_key.decode())
