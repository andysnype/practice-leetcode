from solution2 import productList, productList2
import unittest


class TestAlgo2Reducer(unittest.TestCase):

    def __init__(self, methodName):
        self.algo = productList
        super().__init__(methodName)

    def test_1(self):
        inputArr = [1]
        result = [1]
        self.assertListEqual(self.algo(inputArr), result)

    def test_2(self):
        inputArr = [1, 2]
        result = [2, 1]
        self.assertListEqual(self.algo(inputArr), result)

    def test_3(self):
        inputArr = [2, 1]
        result = [1, 2]
        self.assertListEqual(self.algo(inputArr), result)

    def test_4(self):
        inputArr = [4, 2, 1, 3]
        result = [6, 12, 24, 8]
        self.assertListEqual(self.algo(inputArr), result)

    def test_5(self):
        inputArr = [1, 1, 1, 1, 0, 1, 1]
        result = [0, 0, 0, 0, 1, 0, 0]
        self.assertListEqual(self.algo(inputArr), result)


class TestAlgo2Cached(unittest.TestCase):
    def __init__(self, methodName):
        self.algo = productList2
        super().__init__(methodName)

    def test_1(self):
        inputArr = [1]
        result = [1]
        self.assertListEqual(self.algo(inputArr), result)

    def test_2(self):
        inputArr = [1, 2]
        result = [2, 1]
        self.assertListEqual(self.algo(inputArr), result)

    def test_3(self):
        inputArr = [2, 1]
        result = [1, 2]
        self.assertListEqual(self.algo(inputArr), result)

    def test_4(self):
        inputArr = [4, 2, 1, 3]
        result = [6, 12, 24, 8]
        self.assertListEqual(self.algo(inputArr), result)

    def test_5(self):
        inputArr = [1, 1, 1, 1, 0, 1, 1]
        result = [0, 0, 0, 0, 1, 0, 0]
        self.assertListEqual(self.algo(inputArr), result)


if __name__ == '__main__':
    unittest.main()
