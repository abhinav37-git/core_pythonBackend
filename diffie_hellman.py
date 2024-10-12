import random

def generate_prime():
    while True:
        p = random.randint(100, 1000)
        if is_prime(p):
            return p

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def diffie_hellman_key_exchange(p, g, a, b):
    A = pow(g, a, p)
    # Bob's public key
    B = pow(g, b, p)

    # Alice's secret key
    k_alice = pow(B, a, p)
    # Bob's secret key
    k_bob = pow(A, b, p)

    return k_alice, k_bob

p = generate_prime()
print("Prime number (p):", p)

g = random.randint(2, p - 1)
print("Primitive root modulo p (g):", g)

a = random.randint(1, p - 1)
print("Alice's private key (a):", a)

b = random.randint(1, p - 1)
print("Bob's private key (b):", b)

k_alice, k_bob = diffie_hellman_key_exchange(p, g, a, b)
print("Alice's secret key (k_alice):", k_alice)
print("Bob's secret key (k_bob):", k_bob)