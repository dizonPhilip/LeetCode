import unittest
from median_of_two_sorted_arrays import Solution

class MedianOfTwoSortedArraysTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums1 = [1,3]
        nums2 = [2]
        ret = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(2, ret)

    def test_2(self):
        nums1 = [1,3]
        nums2 = [5]
        ret = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(3, ret)
    
    def test_3(self):
        nums1 = [2,3]
        nums2 = [1]
        ret = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(2, ret)

    def test_4(self):
        nums1 = [2,3,4,5,6,7]
        nums2 = [10]
        ret = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(5, ret)

if __name__ == "__main__":
    unittest.main()