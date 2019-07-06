import unittest
from kth_largest_element_in_a_stream import KthLargest

class KthLargestTest(unittest.TestCase):
    def test_1(self):
        kth_largest = KthLargest(3, [4,5,8,2])
        self.assertEqual(4, kth_largest.add(3))
        self.assertEqual(5, kth_largest.add(5))
        self.assertEqual(5, kth_largest.add(10))
        self.assertEqual(8, kth_largest.add(9))
        self.assertEqual(8, kth_largest.add(4))

    def test_empty_initial_list(self):
        kth_largest = KthLargest(3, [])
        self.assertEqual(3, kth_largest.add(3))
        self.assertEqual(3, kth_largest.add(5))
        self.assertEqual(3, kth_largest.add(10))
        self.assertEqual(5, kth_largest.add(9))
        self.assertEqual(5, kth_largest.add(4))

    def test_2(self):
        kth_largest = KthLargest(2, [0])
        self.assertEqual(-1, kth_largest.add(-1))
        self.assertEqual(0, kth_largest.add(1))
        self.assertEqual(0, kth_largest.add(-2))
        self.assertEqual(0, kth_largest.add(-4))
        self.assertEqual(1, kth_largest.add(3))

if __name__ == "__main__":
    unittest.main()