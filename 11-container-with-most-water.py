from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        iterL = 0
        iterR = len(height) - 1
        maxVol = 0

        while iterL < len(height) and iterR > 0:
            lowerH = min(height[iterR], height[iterL])
            currVol = (iterR - iterL) * lowerH

            if currVol > maxVol:
                maxVol = currVol
            
            if height[iterR] > height[iterL]:
                iterL += 1
            else:
                iterR -= 1

        return maxVol
    

    height = [1,1]
    maxArea(0, height)