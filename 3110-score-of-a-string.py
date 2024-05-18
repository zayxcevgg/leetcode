class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        diff = 0
        while i < len(s)-1:
            diff += abs(ord(s[i]) - ord(s[i+1]))
            i += 1
        
        return diff
            

    s = "hello"
    scoreOfString(0, s)