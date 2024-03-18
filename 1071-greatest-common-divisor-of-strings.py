class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)

        for i in range(min(len(str1), len(str2)), 0, -1):
            if n1 % i or n2 % i:
                continue
            coef1, coef2 = len(str1) // i, len(str2) // i
            base = str1[:i]
            if str1 == coef1 * base and str2 == coef2 * base:
                print(str1[:i])
                return str1[:i]
            else:
                return ""


    str1 = "LEET"
    str2 = "CODE"

    gcdOfStrings(0, str1, str2)