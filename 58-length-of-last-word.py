class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print(len(s.split()[-1]))
        return len(s.split()[-1])


    s = "   fly me   to   the moon  "
    lengthOfLastWord(0, s)