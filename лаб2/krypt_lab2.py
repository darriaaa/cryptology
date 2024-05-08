def KSA(key):
    # Ініціалізуємо S-Box
    key_length = len(key)
    S = list(range(256))  # Створюємо масив S довжиною 256 зі значеннями від 0 до 255
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256  # Використовуємо ключ для змішування S-Box
        S[i], S[j] = S[j], S[i]  # Перестановка елементів у S-Box
    return S

def PRGA(S):
    # Генерація потоку ключів
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Перестановка елементів у S-Box
        K = S[(S[i] + S[j]) % 256]  # Вибір псевдовипадкового байту
        yield K

def RC4(key):
    # Викликаємо функцію KSA для ініціалізації S-Box та генерації потоку ключів
    S = KSA(key)
    return PRGA(S)

def encrypt(message, key):
    # Використовуємо потік ключів RC4 для шифрування повідомлення
    keystream = RC4(key)
    return bytes([message_byte ^ next(keystream) for message_byte in message])

def decrypt(ciphertext, key):
    # Для дешифрування використовуємо ту саму логіку, що і для шифрування
    # Зверніть увагу, що для дешифрування ми також використовуємо функцію encrypt,
    # оскільки RC4 є потоковим шифром, а шифрування і дешифрування виконуються однаковими діями
    decrypted_bytes = encrypt(ciphertext, key)
    return decrypted_bytes.decode()  # Повертаємо рядок Unicode

if __name__ == "__main__":
    # Приклад
    message = b"Hello, world!"  # Вхідне повідомлення
    key = b"secret"  # Ключ

    # Шифруємо повідомлення та виводимо результат
    encrypted_message = encrypt(message, key)
    print("Encrypted message:", encrypted_message)

    # Дешифруємо зашифроване повідомлення та виводимо результат
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)
