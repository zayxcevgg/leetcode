class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iterS = 0
        iterT  = 0

        while iterS < len(s) and iterT < len(t):
            if s[iterS] == t[iterT]:
                iterS += 1
            iterT += 1
    
        return iterS == len(s)
    
    s = "ab"
    t = "baab"
    isSubsequence(0, s, t)