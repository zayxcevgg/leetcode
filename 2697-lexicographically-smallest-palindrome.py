class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        half = len(s) // 2

        for i in range(half):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                s[i] = s[j] = min(s[i], s[j])

        return ''.join(s)

    s = "ab"
    makeSmallestPalindrome(0, s)