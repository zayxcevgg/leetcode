class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        product = 1
        sum = 0
        for i in n:
            product *= int(i)
            sum += int(i)
        return product - sum

    n = 234
    subtractProductAndSum(0, n)

