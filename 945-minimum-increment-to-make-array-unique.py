from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ncounter = 0
        counter = 0
        for n in nums:
            ncounter = max(ncounter, n) 
            counter += ncounter - n
            ncounter += 1

        return counter
        print(counter)
    
    nums = [3,2,1,2,1,7]
    minIncrementForUnique(0, nums)