from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = []

        if len(nums1) > len(nums2):
            shorter = nums2
            longer = nums1
        else:
            shorter = nums1
            longer = nums2

        for i in range(0, len(shorter)):
            if shorter[i] in longer:
                longer.remove(shorter[i])
                res.append(shorter[i])

        print(res)
        return res
    
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    intersect(0, nums1, nums2)