import random
from typing import List, Tuple

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return n == 2
    d = 3
    while ((d ** 2) <= n) and ((n % d) != 0):
        d += 2
    return d * d > n

def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e: int, phi: int) -> int:
    return extended_gcd(e, phi)[1] % phi

def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Оба числа должны быть простыми.")
    elif p == q:
        raise ValueError("p и q не могут быть равны")

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk: Tuple[int, int], plaintext: str) -> List[int]:
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk: Tuple[int, int], ciphertext: List[int]) -> str:
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return "".join(plain)

if __name__ == "__main__":
    print(multiplicative_inverse(7, 40))
    print("RSA Шифровщик/Дешифровщик")
    p = int(input("Введите простое число (17, 19, 23 и т.д.): "))
    q = int(input("Введите другое простое число (не то, что вы ввели выше): "))
    print("Генерация ваших открытого/закрытого ключей . . .")
    public, private = generate_keypair(p, q)
    print("Ваш открытый ключ: ", public, ", а ваш закрытый ключ: ", private)
    message = input("Введите сообщение для шифрования вашим закрытым ключом: ")
    encrypted_msg = encrypt(private, message)
    print("Ваше зашифрованное сообщение: ")
    print("".join(map(lambda x: str(x), encrypted_msg)))
    print("Дешифрование сообщения с использованием открытого ключа ", public, " . . .")
    print("Ваше сообщение:")
    print(decrypt(public, encrypted_msg))
