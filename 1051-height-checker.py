from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        mismatch = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch += 1
        return mismatch
        print(heights, expected, mismatch)

    heights = [1,2,3,4,5]
    heightChecker(0, heights)