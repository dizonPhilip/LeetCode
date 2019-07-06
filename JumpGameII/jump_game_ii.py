from typing import List

class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return 0
        
    #     if nums[0] >= len(nums) - 1:
    #         return 1

    #     num_jumps_performed = 1
    #     index = 1
    #     while True:
    #         max_jump_amount = None
    #         calc_index = 0
    #         i=0
    #         for v in nums[index:index+nums[index-1]]:
    #             jump_amount = (i+index) + v
    #             if max_jump_amount is None or max_jump_amount < jump_amount:
    #                 max_jump_amount = jump_amount
    #                 calc_index = i+index
    #             i += 1
    #         num_jumps_performed += 1
    #         index = calc_index + 1
    #         if (index + nums[calc_index]) >= len(nums):
    #             break

    #     return num_jumps_performed

    def jump(self, nums: List[int]) -> int:
        list_length = len(nums)
        if list_length == 1:
            return 0
        
        if nums[0] >= list_length - 1:
            return 1

        num_jumps_performed = 1
        index = 1
        while True:
            max_jump_amount = None
            calc_index = 0
            for i in range(nums[index-1]):
                refactor = i+index
                jump_amount = nums[refactor] + refactor
                if jump_amount >= list_length:
                    return num_jumps_performed + 1
                if max_jump_amount is None or max_jump_amount <= jump_amount:
                    max_jump_amount = jump_amount
                    calc_index = refactor
            num_jumps_performed += 1
            index = calc_index + 1
            if (index + nums[calc_index]) >= list_length:
                break
            
        return num_jumps_performed
