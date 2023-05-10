# pylint: disable=missing-docstring

import unittest
from max_element_recursive import max_recursive


class TestSearch(unittest.TestCase):
    def test_not_empty(self):
        self.assertEqual(max_recursive([1,2,300,4,100]),300)
    def test_empty(self):
        self.assertEqual(max_recursive([]),0)

if __name__ == '__main__':
    unittest.main()
