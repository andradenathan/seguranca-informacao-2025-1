from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random


def simplified_diffie_helman():
    g, p = 5, 23

    user_a_private_key = random.randint(1, 10)
    user_b_private_key = random.randint(1, 10)

    A_public_key = pow(g, user_a_private_key, p)
    B_public_key = pow(g, user_b_private_key, p)

    shared_key_a = pow(B_public_key, user_a_private_key, p)
    shared_key_b = pow(A_public_key, user_b_private_key, p)

    print(f"Alice envia A = {A_public_key}")
    print(f"Bob envia B = {shared_key_b}")
    print(f"Chave compartilhada (Alice): {shared_key_a}")
    print(f"Chave compartilhada (Bob):   {shared_key_b}")


key = RSA.generate(2048)
public_key = key.publickey()
encryptor = PKCS1_OAEP.new(public_key)
decryptor = PKCS1_OAEP.new(key)

message = b"original $ message $"
ciphertext = encryptor.encrypt(message)
plaintext = decryptor.decrypt(ciphertext)

print("🔐 RSA")
print(f"Mensagem criptografada: {ciphertext[:30]}...")
print(f"Mensagem decriptada: {plaintext}")


print("\n🔐 Diffie-Hellman (exemplo simplificado)")
simplified_diffie_helman()
