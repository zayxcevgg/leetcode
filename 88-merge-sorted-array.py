from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tomerge = nums1[:m]
        tomerge += nums2[:n]
        tomerge.sort()
        nums1 = tomerge
        
        for i, j in enumerate(nums1):
           nums1[j] = tomerge[j]
           
        print(nums1)
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(0, nums1, m, nums2, n)