from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNums1 = set(nums1)
        setNums2 = set(nums2)
        onlyNums1 = set()
        onlyNums2 = set()

        for num in nums1:
            if num not in nums2:
                onlyNums1.add(num)

        for num in nums2:
            if num not in nums1:
                onlyNums2.add(num)

        return [list(onlyNums1), list(onlyNums2)]

    nums1 = [1,2,3]
    nums2 = [2,4,6]
    findDifference(0, nums1, nums2)