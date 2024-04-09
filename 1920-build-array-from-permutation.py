from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in nums:
            res[i] = nums[nums[i]]
        print(res)
        return res

    nums = [0,2,1,5,3,4]
    buildArray(0, nums)