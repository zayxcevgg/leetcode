class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        for num in nums:
            if num in seen:
                pass
            else:
                seen.append(num)
        nums = seen
        return len(nums)
    
obj = Solution()
nums = [1,1,2]
obj.removeDuplicates(nums)