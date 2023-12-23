
import string
import vigenere
from unittest import TestCase
from caesar import encrypt_caesar, decrypt_caesar
import random


class CalculatorTestCase(TestCase):
    def test_encrypt_small(self) -> None:
        self.assertEqual(encrypt_caesar('python'), 'sbwkrq')

    def test_encrypt_big(self) -> None:
        self.assertEqual(encrypt_caesar('PYTHON'), 'SBWKRQ')

    def test_encrypt_capitalize(self) -> None:
        self.assertEqual(encrypt_caesar('Python3.6'), 'Sbwkrq3.6')

    def test_encrypt_clear(self) -> None:
        self.assertEqual(encrypt_caesar(''), '')

    def test_encrypt_symbols(self) -> None:
        self.assertEqual(encrypt_caesar('4358768^%^%#^%$7889865????*******31354.'),
                         '4358768^%^%#^%$7889865????*******31354.')

    def test_decrypt_small(self) -> None:
        self.assertEqual(decrypt_caesar('sbwkrq'), 'python')

    def test_decrypt_big(self) -> None:
        self.assertEqual(decrypt_caesar('SBWKRQ'), 'PYTHON')

    def test_decrypt_capitalize(self) -> None:
        self.assertEqual(decrypt_caesar('Sbwkrq3.6'), 'Python3.6')

    def test_decrypt_small(self) -> None:
        self.assertEqual(decrypt_caesar(''), '')

    def test_decrypt_symbols(self) -> None:
        self.assertEqual(decrypt_caesar('4358768^%^%#^%$7889865????*******31354.'),
                         '4358768^%^%#^%$7889865????*******31354.')

    def test_randomized(self, random=None):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = vigenere.encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, vigenere.decrypt_vigenere(ciphertext, keyword))