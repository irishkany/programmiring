import unittest
import калькулятор

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(2, 5), -3)
        self.assertEqual(sub(0, 0), 0)

    def test_mult(self):
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(-2, 3), -6)
        self.assertEqual(mult(0, 5), 0)

    def test_div(self):
        self.assertEqual(div(6, 3), 2)
        self.assertEqual(div(-6, 3), -2)
        self.assertEqual(div(0, 5), 0)
        self.assertEqual(div(6, 0), "Ошибка")

if __name__ == '__main__':
    unittest.main()