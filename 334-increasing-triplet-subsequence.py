from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxNums = [0] * len(nums)
        maxNums[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            maxNums[i] = max(maxNums[i+1], nums[i+1])
            
        minNums = nums[0]
        for i in range(1, len(nums)-1):
            if minNums < nums[i] < maxNums[i]:
                return True
            minNums = min(minNums, nums[i])
        return False
                    
    nums = [1,5,0,4,1,3]
    increasingTriplet(0, nums)