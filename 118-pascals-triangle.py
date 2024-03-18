from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        
        resTriangle = [[1]]
        for row in range(0, numRows):
            lastRow = resTriangle[-1]
            currRow = [1]
            for i in range(1, len(lastRow)):
                currRow.append(lastRow[i - 1] + lastRow[i])
            currRow.append(1)
            resTriangle.append(currRow)
        print(resTriangle)
            
        
    numRows = 30
    generate(0, numRows)