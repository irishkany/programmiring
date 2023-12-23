def encrypt_caesar(plaintext: str, shift: int = 3) -> str:  
    ciphertext = ''
    shift %= 26
    for i in plaintext:
        old_ord = ord(i)
        if (old_ord > 64) and (old_ord < 91):
            new_ord = old_ord + shift
            if new_ord > 90:
                new_ord = 65 + shift - 90 + old_ord - 1
        elif (old_ord > 96) and (old_ord < 123):
            new_ord = old_ord + shift
            if new_ord > 122:
                new_ord = 97 + shift - 122 + old_ord - 1
        else:
            new_ord = old_ord
        ciphertext += chr(new_ord)
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ''
    shift %= 26
    for i in ciphertext:
        old_ord = ord(i)
        if (old_ord > 64) and (old_ord < 91):
            new_ord = old_ord - shift
            if new_ord < 65:
                new_ord = 90 - shift + 65 - old_ord + 3
        elif (old_ord > 96) and (old_ord < 123):
            new_ord = old_ord - shift
            if new_ord < 97:
                new_ord = 122 - shift + 97 - old_ord + 3
        else:
            new_ord = old_ord
        plaintext += chr(new_ord)
    return plaintext

if __name__ == '__main__':
    print(encrypt_caesar(input()))
    print(decrypt_caesar(input()))
    print(encrypt_caesar('dssgeauyfg isguoYGIYTFUYGIGHvljhvkIUTRUYRIUTI^%%^$^%$^*&*(%^#%^$hgcfkuyKFYTDFCUGHKJYgkJBLJhvkjn465165435465645....u^%$^#$^&^*^^$%^$%&nnn', 24) == 'bqqecyswd
