import unittest
from fib import fib

class TestFibonacci(unittest.TestCase):
    def test_fib_0(self):
        self.assertEqual(fib(0), 1)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_2(self):
        self.assertEqual(fib(2), 2)

    def test_fib_3(self):
        self.assertEqual(fib(3), 3)

    def test_fib_4(self):
        self.assertEqual(fib(4), 5)

if __name__ == "__main__":
    unittest.main()
