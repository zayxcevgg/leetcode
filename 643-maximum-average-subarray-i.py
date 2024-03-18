from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n < k: 
            return -1
        
        window_sum = sum(nums[:k])
        window_max = window_sum
        
        for i in range(n - k):
            window_curr = nums[i:i + k]
            window_sum = window_sum - nums[i] + nums[i+k]
            window_max = max(window_max, window_sum)
        print(window_max/k)
        return window_max/k

    nums = [1,12,-5,-6,50,3]
    k = 4
    findMaxAverage(0, nums, k)