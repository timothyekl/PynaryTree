import unittest

from PynaryTree import *

class TestInsert(unittest.TestCase):
    
    def setUp(self):
        self.root = TreeNode(5)

    def test_one_insert(self):
        self.root.insert(8)
        self.assertEqual(str(self.root), '58')

    def test_weird_insert(self):
        self.root.insert(TreeNode(3))
        self.assertEqual(str(self.root), '35')

    def test_mult_insert(self):
        self.root.insert(8)
        self.root.insert(3)
        self.root.insert(1)
        self.root.insert(4)
        self.root.insert(9)
        self.root.insert(6)
        self.assertEqual(str(self.root), '1345689')

if __name__ == '__main__':
    unittest.main()
