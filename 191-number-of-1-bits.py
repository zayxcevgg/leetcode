class Solution:
    def hammingWeight(self, n: int) -> int:
        b = "{0:b}".format(n)
        return b.count("1")

sol = Solution()
n = 2147483645
sol.hammingWeight(n)
        