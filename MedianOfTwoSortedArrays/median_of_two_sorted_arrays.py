from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num_iterations_to_median = (len(nums1) + len(nums2)) // 2
        num_iterations_to_median += 1

        need_to_average = False if (len(nums1) + len(nums2)) % 2 else True

        index1 = 0
        index2 = 0

        previous_median = None
        median = None
        for _ in range(num_iterations_to_median):
            previous_median = median
            if index2 >= len(nums2):
                median = nums1[index1]
                index1 += 1
            elif index1 >= len(nums1):
                median = nums2[index2]
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                median = nums1[index1]
                index1 += 1
            else:
                median = nums2[index2]
                index2 += 1

        if need_to_average:
            median = (previous_median + median) / 2
        return median


#######################################################################################
#
# simple solution
#
# import itertools
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         sorted_list = sorted(itertools.chain(nums1, nums2))
#         median_index = len(sorted_list) // 2
#         if len(sorted_list) % 2 == 0:
#             return (sorted_list[median_index-1] + sorted_list[median_index]) / 2
#         else:
#             return sorted_list[median_index]
