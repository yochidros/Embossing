import base64
from Crypto import Random
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key, block_size=32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

    def encrypt(self, raw_data):
        raw_data = self._pad(raw_data)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw_data))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        print(enc)
        print(iv)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))

    def _pad(self, passphrase):
        f = (self.bs - len(passphrase) % self.bs)
        return passphrase + f * chr(f)

    def _unpad(self, padedphrase):
        return padedphrase[:-ord(padedphrase[len(padedphrase)-1:])]
