from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        axisx = []
        for i in points:
            axisx.append(i[0])
        axisx = sorted(axisx)
        res = max([axisx[j+1]-axisx[j] for j in range(len(axisx)-1)])   
        return res

    points = [[8,7],[9,9],[7,4],[9,7]]
    maxWidthOfVerticalArea(0, points)