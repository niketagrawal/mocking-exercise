import unittest
from exp import mod

class TestSum(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mod.add(2, 4), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()