import numpy as np
import pandas as pd
from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        print(grid, len(grid[0]))
        for i in range(len(grid[0])):
            print(i)
            maxlen = 0
            for j in range(len(grid)):
                maxlen = max(maxlen, len(str(grid[j][i])))
            ans.append(maxlen)
        return(ans)
    
    findColumnWidth(0, [[-15,1,3],[15,7,12],[5,6,-2]])
    findColumnWidth(0, [[1],[22],[333]])