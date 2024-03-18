from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0] * len(nums)        
        runningSum[0] = nums[0]
        for i in range(1, len(nums)):
            runningSum[i] = runningSum[i-1] + nums[i]
            nums[i] = runningSum[i] 
        return(runningSum)

    runningSum(0,[1,1,1,1])

# Good Solution
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         for i in range(1, len(nums)):
#             nums[i] = nums[i] + nums[i-1]
#         return nums
        