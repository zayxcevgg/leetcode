class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        difference = 0
        for letter in s:
            difference += abs(s.index(letter) - t.index(letter)) 
        return difference
    
    s = "abcde"
    t = "edbac"
    findPermutationDifference(0, s, t)