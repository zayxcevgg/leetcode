from collections import defaultdict
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dict = []
        for i in range(0, len(grid)):
            horizontal = int(''.join(map(str, grid[i])))
            vertical = ''
            for j in range(0, len(grid)):
                vertical += str(grid[j][i])
            dict.append((horizontal, int(vertical)))
        
        matches = 0
        for key, value in dict:
            if key in [v for k, v in dict]:
                matches += 1
        print(matches)
        return matches


    grid = [[3,1,2,2]
            [1,4,4,4],
            [2,4,2,2],
            [2,5,2,2]]
    equalPairs(0, grid)