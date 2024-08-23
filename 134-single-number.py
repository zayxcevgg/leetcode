from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num

        print(unique)

        return unique
    
sol = Solution()
nums = [4,1,2,1,2]
sol.singleNumber(nums)