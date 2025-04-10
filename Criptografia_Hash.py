import hashlib

# Entrada de dados
mensagem = "Essa é uma mensagem que será transformada em hash"

# Cria o hash SHA-256
hash_obj = hashlib.sha256(mensagem.encode())

# Converte o hash para string hexadecimal
hash_hex = hash_obj.hexdigest()

print("Mensagem original:", mensagem)
print("Hash SHA-256:", hash_hex)
