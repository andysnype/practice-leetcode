from solution1 import problem1
import unittest


class TestAlgo1(unittest.TestCase):

    def __init__(self, methodName):
        self.algo = problem1
        super().__init__(methodName)

    def test_1(self):
        arr = []
        k = 15
        self.assertFalse(self.algo(arr, k))

    def test_2(self):
        arr = [10, 15, 3, 7]
        k = 17
        self.assertTrue(self.algo(arr, k))

    def test_3(self):
        arr = [41, 15, 245242, -24]
        k = 17
        self.assertTrue(self.algo(arr, k))


if __name__ == '__main__':
    unittest.main()
