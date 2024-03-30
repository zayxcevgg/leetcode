from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, j in enumerate(index):
            target.insert(j, nums[i])
        return target

    nums = [0,1,2,3,4]
    index = [0,1,2,2,1]
    createTargetArray(0, nums, index)