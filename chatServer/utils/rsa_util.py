from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto import Random
from base64 import b64decode,b64encode

def rsa_decrypt(message):
    dsize = SHA.digest_size
    private_key = RSA.import_key(open("rsa/private.pem").read())
    cipher_rsa = PKCS1_v1_5.new(private_key)
    sentinel = Random.new().read(4096 + dsize)
    return cipher_rsa.decrypt(b64decode(message), sentinel).decode()

def rsa_encrypt(message):
     # 字符串指定编码（转为bytes）
    message = message.encode('utf-8')
    public_key = RSA.import_key(open("rsa/public.pem").read())
    cipher_rsa = PKCS1_v1_5.new(public_key)
    text_encrypted = cipher_rsa.encrypt(message)
    text_encrypted_base64 = b64encode(text_encrypted).decode()
    return text_encrypted_base64 