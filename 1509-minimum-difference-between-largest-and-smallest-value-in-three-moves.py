from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
        if nums_len <= 4:
            return 0
        
        min_diff = 99999999999999999999
        nums.sort()
        
        for left in range(4):
            right = nums_len - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])

        return min_diff
    
    nums = [3,100,20]
    minDifference(0, nums)