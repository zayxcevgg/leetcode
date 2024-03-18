from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        iter = 0
        numsLen = len(nums) - 1
        while iter <= numsLen:
            mid = (iter + numsLen) // 2
            if nums[mid] < target:
                iter = mid + 1
            elif nums[mid] > target:
                numsLen = mid - 1
            else:
                return mid
        return iter

    class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
        

    nums = [1,3,5,6]
    target = 5
    searchInsert(0, nums, target)