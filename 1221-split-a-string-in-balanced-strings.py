class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        l = 0
        pair = 0
        for i in s:
            if i == 'L':
                l += 1
            if i == 'R':
                r += 1
            if r == l:
                pair += 1
        
        return pair

    s = "RLRRLLRLRL"
    balancedStringSplit(0, s)