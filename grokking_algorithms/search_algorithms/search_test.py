# pylint: disable=missing-docstring

import unittest
from binary_search import binary_search
from simple_search import simple_search

class TestSearch(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.array = list(range(1,1001))
    def test_simple_found(self):
        self.assertEqual(simple_search(self.array,500),499)
    def test_binary_found(self):
        self.assertEqual(binary_search(self.array,500),499)
    def test_simple_not_found(self):
        self.assertEqual(simple_search(self.array,-5),None)
    def test_binary_not_found(self):
        self.assertEqual(binary_search(self.array,-5),None)

if __name__ == '__main__':
    unittest.main()
