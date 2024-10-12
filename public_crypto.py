from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key

private_key = generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()  # Obtain public key from private key

plaintext = b"Encryption! Text"
ciphertext = public_key.encrypt(
    plaintext,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

decrypted_plaintext = private_key.decrypt(
    ciphertext,
    asymmetric.padding.OAEP(
        mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)