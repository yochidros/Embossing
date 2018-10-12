from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


data = 'hello'
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(chiphertext)


