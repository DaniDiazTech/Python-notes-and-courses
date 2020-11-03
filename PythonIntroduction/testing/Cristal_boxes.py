import unittest

def is_adult(age):
    if age >= 18:
        return True
    else:
        return False


class CristalTest(unittest.TestCase):
    def test_is_adult(self):
        age1 = 19

        result = is_adult(age1)

        self.assertEqual(result, True)

    def test_is_not_adult(self):
        age2 = 15

        result = is_adult(age2)

        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)   