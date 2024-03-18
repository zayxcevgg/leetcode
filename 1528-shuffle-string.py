from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        for i in range(len(s)):
            place = indices[i]
            res[place] = s[i]

        return ''.join(res)

    
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    restoreString(0, s, indices)
            