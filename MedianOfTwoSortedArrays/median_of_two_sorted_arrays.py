from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0

        total_len = len(nums1) + len(nums2)
        median_index = total_len // 2
        need_to_get_average = False
        if total_len % 2:
            need_to_get_average = True


        median = 0
        logical_index1 = 0
        logical_index2 = 0
        middle = 0
        while True:
            if nums1[index1] <= nums2[index2]:
                if index1 == len(nums1) - 1:
                    index2 += 1
                else:
                    index1 += 1
            elif nums2[index2] < nums1[index1]:
                if index2 == len(nums2) - 1:
                    index1 += 1
                else:
                    index2 += 1
            count += 1
            if count == median_index:
                if nums1[index1] <= nums2[index2]:
                    median = nums1[index1]
                else:
                    median = nums2[index2]
                break
        
        return median