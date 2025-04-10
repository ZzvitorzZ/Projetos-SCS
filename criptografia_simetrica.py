from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Geração de chave e dados
chave = get_random_bytes(16)  # AES-128
cipher = AES.new(chave, AES.MODE_EAX)

# Texto a ser criptografado
mensagem = b'Essa e uma mensagem secreta!'
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(mensagem)

print("Mensagem criptografada:", base64.b64encode(ciphertext).decode())
print("Chave:", base64.b64encode(chave).decode())
print("Nonce:", base64.b64encode(nonce).decode())

cipher_decrypt = AES.new(chave, AES.MODE_EAX, nonce=nonce)
mensagem_descriptografada = cipher_decrypt.decrypt(ciphertext)

print("Mensagem descriptografada:", mensagem_descriptografada.decode())

