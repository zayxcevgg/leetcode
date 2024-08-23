from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for number in range(0, len(nums)):
            if nums[number] % 2 == 0:
                nums[number] = 0
            else:
                nums[number] = 1

        prefix_sum = 0
        nice_sub = 0
        prefix_dict= defaultdict(int)
        prefix_dict[0] = 1

        for num in nums:
            prefix_sum += num
        
            if (prefix_sum - k) in prefix_dict:
                nice_sub += prefix_dict[prefix_sum - k]
            
            prefix_dict[prefix_sum] += 1
        return nice_sub
        
        
    nums = [1,1,2,1,1]
    k = 3
    numberOfSubarrays(0, nums, k)