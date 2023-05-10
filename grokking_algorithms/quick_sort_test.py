# pylint: disable=missing-docstring

import unittest
from quick_sort import quick_sort

class TestSort(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.array = [5,4,3,-3,2,1]
    def test_quicksort(self):
        self.assertEqual(quick_sort(self.array),[-3,1,2,3,4,5])
    def test_quicksort_empty(self):
        self.assertEqual(quick_sort([]),[])

if __name__ == '__main__':
    unittest.main()
