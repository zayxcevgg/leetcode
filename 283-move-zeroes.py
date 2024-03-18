from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)-1
        while n >= 0:
            if nums[n] == 0:
                nums.pop(n)
                nums.append(0)
            n -= 1

    nums = [0,0,1]
    moveZeroes(0, nums)