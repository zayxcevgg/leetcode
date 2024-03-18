from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    pairs += 1

        print(pairs)



    nums = [1,2,3,1,1,3]
    numIdenticalPairs(0, nums)