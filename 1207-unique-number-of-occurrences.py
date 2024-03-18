from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        for num in set(arr):
            map[num] = arr.count(num)
        if len(list(map.values())) == len(set(list(map.values()))):
            return True
        else:
            return False
            
        
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    uniqueOccurrences(0, arr)