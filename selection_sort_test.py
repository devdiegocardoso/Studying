# pylint: disable=missing-docstring

import unittest
from selection_sort import selection_sort

class TestSort(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.array = [5,4,3,-3,2,1]
    def test_selection(self):
        self.assertEqual(selection_sort(self.array),[-3,1,2,3,4,5])
    
if __name__ == '__main__':
    unittest.main()
