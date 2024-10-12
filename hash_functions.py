import hashlib

md5_hash = hashlib.md5(b"SHA HASH 1").hexdigest()
print("MD5 hash:", md5_hash)

sha256_hash = hashlib.sha256(b"SHA HASH 2").hexdigest()
print("SHA-256 hash:", sha256_hash)

sha512_hash = hashlib.sha512(b"SHA HASH 3").hexdigest()
print("SHA-512 hash:", sha512_hash)