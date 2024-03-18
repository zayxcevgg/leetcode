from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        iterL = 0
        iterR = len(nums) - 1
        ops = 0

        nums = sorted(nums)

        while iterL < iterR:
            if nums[iterL] + nums[iterR] > k:
                iterR -= 1
            elif nums[iterL] + nums[iterR] < k:
                iterL += 1
            else:
                iterL += 1
                iterR -= 1
                ops += 1
            
        return ops
        
    
    nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4]
    k = 2
    maxOperations(0, nums, k)