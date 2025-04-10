from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Gera par de chaves (pública e privada)
chave = RSA.generate(2048)
chave_publica = chave.publickey()

# Cria objeto de criptografia com chave pública
cipher_rsa_encrypt = PKCS1_OAEP.new(chave_publica)

# Mensagem original
mensagem = b'Essa e uma mensagem secreta com RSA!'

# Criptografa
mensagem_criptografada = cipher_rsa_encrypt.encrypt(mensagem)

# Cria objeto de descriptografia com chave privada
cipher_rsa_decrypt = PKCS1_OAEP.new(chave)

# Descriptografa
mensagem_descriptografada = cipher_rsa_decrypt.decrypt(mensagem_criptografada)

# Mostra resultados
print("Mensagem criptografada:", base64.b64encode(mensagem_criptografada).decode())
print("Mensagem descriptografada:", mensagem_descriptografada.decode())
#Exibe a chave privada
print(chave.export_key().decode())
#Exibe Chave Privada
print(chave.publickey().export_key().decode())