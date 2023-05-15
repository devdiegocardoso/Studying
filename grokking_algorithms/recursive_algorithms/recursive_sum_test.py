# pylint: disable=missing-docstring

import unittest
from recursive_sum import recursive_sum


class TestSearch(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.numbers_1 = [1,2,3]
        self.numbers_2 = [2,4,6,8,10]
        self.numbers_3 = [-2,-4,-6]
        self.numbers_4 = []
    def test_sequence(self):
        self.assertEqual(recursive_sum(self.numbers_1,len(self.numbers_1)-1),6)
    def test_evens(self):
        self.assertEqual(recursive_sum(self.numbers_2,len(self.numbers_2)-1),30)
    def test_negatives(self):
        self.assertEqual(recursive_sum(self.numbers_3,len(self.numbers_3)-1),-12)
    def test_empty(self):
        self.assertEqual(recursive_sum(self.numbers_4,len(self.numbers_4)-1),0)

if __name__ == '__main__':
    unittest.main()
