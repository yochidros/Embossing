import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class AESCipher(object):
    def __init__(self, key, iv, block_size=32):
        self.bs = block_size
        self.iv = iv
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

        backend = default_backend()
        self.cipher = Cipher(
            algorithms.AES(self.key), 
            modes.CBC(self.iv), 
            backend=backend
        )

    def encrypt(self, raw_data):
        raw_data = self._pad(raw_data)
        raw_data = raw_data.encode()
        encryptor = self.cipher.encryptor()
        ct = encryptor.update(raw_data) + encryptor.finalize()
        return base64.b64encode(ct)

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        decryptor = self.cipher.decryptor()
        dt = decryptor.update(enc) + decryptor.finalize()
        return self._unpad(dt).decode()

    def _pad(self, passphrase):
        f = (self.bs - len(passphrase) % self.bs)
        return passphrase + f * chr(f)

    def _unpad(self, padedphrase):
        return padedphrase[:-ord(padedphrase[len(padedphrase)-1:])]
    

