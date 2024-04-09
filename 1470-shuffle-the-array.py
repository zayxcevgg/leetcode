from typing import List
import numpy as np

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
        

           

    nums = [2,5,1,3,4,7]
    n = 3
    shuffle(0, nums, n)