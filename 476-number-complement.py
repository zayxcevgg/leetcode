class Solution:
    def findComplement(self, num: int) -> int:
        bin = "{0:b}".format(num)
        bin = bin.replace("1", "X")
        bin = bin.replace("0", "1")
        bin = bin.replace("X", "0")
        
        res = int(bin, 2)
        return res



sol = Solution()
num = 1
sol.findComplement(num)