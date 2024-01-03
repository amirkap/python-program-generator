import unittest


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Error: Division by zero")
    return x / y


class Calculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 2), 7)
        self.assertEqual(add(-3, 5), 2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(100, -100), 0)
        self.assertEqual(add(2.5, 3.7), 6.2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(-3, 5), -8)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(100, -100), 200)
        self.assertEqual(subtract(2.5, 1.7), 0.8)

    def test_multiply(self):
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(100, -100), -10000)
        self.assertEqual(multiply(2.5, 3.7), 9.25)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-15, 5), -3)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(100, -10), -10)
        self.assertEqual(divide(2.5, 1.25), 2)

        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()