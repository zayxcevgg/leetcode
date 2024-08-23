from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        for num1 in range(0, len(nums)):
            sum += nums[num1]
            for num2 in range(num1, len(nums) - num1):
                sum += nums[num1] ^ nums[num2]

        print(sum)
    
    nums = [5,1,6]
    subsetXORSum(0, nums)
