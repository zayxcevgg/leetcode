from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if i >= 0 and i < j and j < len(nums) and nums[i] + nums[j] < target:
                    pairs += 1
            
        return pairs

    nums = [-1,1,2,3,1]
    target = 2
    countPairs(0, nums, target)
