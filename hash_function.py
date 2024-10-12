import hashlib

def create_hash(message, salt):
    """Creates a SHA-256 hash of the message with the given salt."""
    return hashlib.sha256((message + salt).encode('utf-8')).hexdigest()

password = "mysecretpassword"
salt = "random_salt"
hashed_password = create_hash(password, salt)
print("Hashed Password:", hashed_password)

message = "Abhinav's key"
private_key = "my_private_key"
signature = create_hash(message, private_key)
print("Digital Signature:", signature)

timestamp = "1695697423"
random_seed = "my_random_seed"
random_number = create_hash(timestamp, random_seed)
print("Random Number:", random_number)