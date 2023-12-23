def next_symbol(ord_symbol: int, shift: int) -> str:
    if (ord_symbol < 65) or ((ord_symbol > 90) and (ord_symbol < 97)) or (ord_symbol > 122) or (shift == 0):
        return chr(ord_symbol)
    if ord_symbol == 90:
        return next_symbol(65, shift - 1)
    if ord_symbol == 122:
        return next_symbol(97, shift - 1)
    return next_symbol(ord_symbol + 1, shift - 1)

def last_symbol(ord_symbol: int, shift: int) -> str:
    if (ord_symbol < 65) or ((ord_symbol > 90) and (ord_symbol < 97)) or (ord_symbol > 122) or (shift == 0):
        return chr(ord_symbol)
    if ord_symbol == 65:
        return last_symbol(90, shift - 1)
    if ord_symbol == 97:
        return last_symbol(122, shift - 1)
    return last_symbol(ord_symbol - 1, shift - 1)

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ''
    keyword = keyword.upper() * (len(plaintext) // len(keyword) + 1)
    for i in range(len(plaintext)):
        ciphertext += next_symbol(ord(plaintext[i]), (ord(keyword[i]) - 65) % 26)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ''
    keyword = keyword.upper() * (len(ciphertext) // len(keyword) + 1)
    for i in range(len(ciphertext)):
        plaintext += last_symbol(ord(ciphertext[i]), (ord(keyword[i]) - 65) % 26)
    return plaintext

if __name__ == '__main__':
    print(encrypt_vigenere(input('Введите строку: '), input('Введите ключ: ')))
    print(decrypt_vigenere(input('Введите строку: '), input('Введите ключ: ')))
