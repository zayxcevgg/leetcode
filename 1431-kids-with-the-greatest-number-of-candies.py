from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ifMax = []
        for kid in candies:
            if kid + extraCandies >= max(candies):
                ifMax.append(True)
            else:
                ifMax.append(False)

        
        print(ifMax)
        return ifMax
 
    candies = [2,3,5,1,3]
    extraCandies = 3
    kidsWithCandies(0, candies, extraCandies)