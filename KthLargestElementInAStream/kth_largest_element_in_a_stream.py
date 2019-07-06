# https://leetcode.com/problems/kth-largest-element-in-a-stream/

from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) < self.k:
                heapq.heappush(self.nums, num)
            elif num > self.nums[0]:
                # don't let the heap grow larger than k elements
                heapq.heappushpop(self.nums, num)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            # don't let the heap grow larger than k elements
            heapq.heappushpop(self.nums, val)
        return self.nums[0]