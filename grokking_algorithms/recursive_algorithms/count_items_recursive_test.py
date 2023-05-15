# pylint: disable=missing-docstring

import unittest
from count_items_recursive import recursive_count


class TestSearch(unittest.TestCase):
    def test_not_empty(self):
        self.assertEqual(recursive_count([1,2,3,4,100]),5)
    def test_empty(self):
        self.assertEqual(recursive_count([]),0)

if __name__ == '__main__':
    unittest.main()
