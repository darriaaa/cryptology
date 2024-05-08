import random

# Функція для знаходження оберненого модулярного
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Генеруємо випадкове просте число
def generate_large_prime(bit_length):
    prime = 4
    while not is_prime(prime):
        prime = random.getrandbits(bit_length)
    return prime

# Перевірка, чи є число простим
def is_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Генеруємо ключі
def generate_keypair(bit_length):
    p = generate_large_prime(bit_length)
    g = random.randint(2, p - 1)
    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    public_key = (p, g, h)
    private_key = x
    return public_key, private_key

# Шифрування
def encrypt(plaintext, public_key):
    p, g, h = public_key
    y = random.randint(2, p - 2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (plaintext * s) % p
    return c1, c2

# Дешифрування
def decrypt(ciphertext, public_key, private_key):
    p, g, h = public_key
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    plaintext = (c2 * modinv(s, p)) % p
    return plaintext

# Приклад
if __name__ == "__main__":
    # Генеруємо ключі
    public_key, private_key = generate_keypair(256)

    # Повідомлення для шифрування
    plaintext = 123456789

    # Шифруємо повідомлення
    ciphertext = encrypt(plaintext, public_key)

    # Дешифруємо повідомлення
    decrypted_plaintext = decrypt(ciphertext, public_key, private_key)

    print("Public key:", public_key)
    print("Private key:", private_key)
    print("Original plaintext:", plaintext)
    print("Decrypted plaintext:", decrypted_plaintext)
