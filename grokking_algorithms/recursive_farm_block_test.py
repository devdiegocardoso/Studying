# pylint: disable=missing-docstring

import unittest
from recursive_farm_block import recursive_block


class TestSearch(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(recursive_block(1680,640),80)
    def test_evens(self):
        self.assertEqual(recursive_block(1050,100),50)
    def test_negatives(self):
        self.assertEqual(recursive_block(1234,2345),1)

if __name__ == '__main__':
    unittest.main()
