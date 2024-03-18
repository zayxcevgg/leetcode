from itertools import count
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0

        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
        
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    
        return count >= n
        
    flowerbed = [1,0,0,0,0,1]
    n = 2
    canPlaceFlowers(0, flowerbed, n)
