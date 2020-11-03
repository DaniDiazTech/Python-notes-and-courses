import unittest

def add(number1, number2):
    return number1 + number2

class BlackBox(unittest.TestCase):

    def test_sum_positive(self):
        n1 = 10
        n2 = 7
        result =  add(n1, n2)

        self.assertEqual(result, 17)
    def test_sum_negatives(self):
        n1 = -5
        n2 = -7

        result = add(n1,n2)

        self.assertEqual(result, -12)

if __name__ == "__main__":
    unittest.main()
