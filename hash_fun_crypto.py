from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"SHA HASH")
sha256_hash = digest.finalize().hex()
print("SHA-256 hash:", sha256_hash)