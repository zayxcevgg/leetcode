class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(0, len(l)):
            l[i] = l[i][::-1]
        return " ".join(l)

    s = "Mr Ding"
    reverseWords(0, s)