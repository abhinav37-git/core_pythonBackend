import rsa
import time
import json

def generate_keys(key_size=2048):
    """Generates a pair of RSA public and private keys."""
    return rsa.newkeys(key_size)

def create_digital_signature(message, private_key, name, honors_name, purpose):
    """Creates a digital signature for the given message."""
    signature = rsa.sign(message.encode('utf-8'), private_key, 'SHA-256')
    data_of_creation = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    data_of_expiration = (time.time() + 365 * 24 * 60 * 60)  # One year from now
    data_of_expiration = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(data_of_expiration))

    signature_data = {
        "name": name,
        "dataOfCreation": data_of_creation,
        "dataOfExpiration": data_of_expiration,
        "honorsName": honors_name,
        "purpose": purpose,
        "signature": signature.hex()
    }

    return json.dumps(signature_data)

def verify_digital_signature(signature_data, message, public_key):
    """Verifies a digital signature."""
    signature_data = json.loads(signature_data)

    # Check expiration
    if time.time() > time.mktime(time.strptime(signature_data["dataOfExpiration"], '%Y-%m-%dT%H:%M:%SZ')):
        return False

    # Verify signature
    try:
        rsa.verify(message.encode('utf-8'), bytes.fromhex(signature_data["signature"]), public_key)
        return True
    except rsa.VerificationError:
        return False

# Example usage
(public_key, private_key) = generate_keys()

message = "This is a message to be signed."
name = "John Doe"
honors_name = "Government Agency"
purpose = "Document Authentication"

signature = create_digital_signature(message, private_key, name, honors_name, purpose)
print(signature)

is_valid = verify_digital_signature(signature, message, public_key)
print("Signature is valid:", is_valid)