from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        srtNums = sorted(nums)
        for i in nums:
            index = srtNums.index(i)
            res.append(index)
        return res

    
    nums = [8,1,2,2,3]
    smallerNumbersThanCurrent(0, nums)