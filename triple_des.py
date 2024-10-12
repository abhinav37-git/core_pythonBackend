from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def triple_des_encrypt(plaintext, key):
    """Encrypts plaintext using 3DES in ECB mode with padding."""
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long for 3DES") 
    des1 = DES.new(key[:8], DES.MODE_ECB)
    des2 = DES.new(key[8:16], DES.MODE_ECB)
    des3 = DES.new(key[16:], DES.MODE_ECB)
    plaintext = pad(plaintext, DES.block_size)
    ciphertext = des1.encrypt(des2.decrypt(des3.encrypt(plaintext)))
    return ciphertext
def triple_des_decrypt(ciphertext, key):
    """Decrypts ciphertext using 3DES in ECB mode with padding removal."""
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long for 3DES")

    des1 = DES.new(key[:8], DES.MODE_ECB)
    des2 = DES.new(key[8:16], DES.MODE_ECB)
    des3 = DES.new(key[16:], DES.MODE_ECB)

    plaintext = des3.decrypt(des2.encrypt(des1.decrypt(ciphertext)))
    return unpad(plaintext, DES.block_size)
key = b"098765432112345678901234"
plaintext = b"This is a secret message"

ciphertext = triple_des_encrypt(plaintext, key)
decrypted_text = triple_des_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted_text.decode()) 