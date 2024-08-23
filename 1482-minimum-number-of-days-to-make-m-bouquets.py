from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        total = m * k 
        if total > len(bloomDay):
            return -1

        bloomDay.sort()
        
        for day in bloomDay:
            total -= bloomDay.count(day)
            if total <= 0:
                return day
                


        return 0
    
    bloomDay = [1,10,3,10,2]
    m = 3
    k = 1
    minDays(0, bloomDay, m, k)