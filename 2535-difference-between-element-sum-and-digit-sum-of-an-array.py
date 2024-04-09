from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for element in nums: 
            for digit in str(element):
                digit_sum += int(digit)
        return sum(nums) - digit_sum

    nums = [1,15,6,3]
    differenceOfSum(0, nums)