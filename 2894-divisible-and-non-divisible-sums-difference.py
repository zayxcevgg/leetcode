class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        for i in range(0, n+1):
            if i % m != 0:
                num1 += i
        
        num2 = 0
        for j in range(0, n+1):
            if j % m == 0:
                num2 += j

        return num1 - num2

        
    n = 10
    m = 3
    differenceOfSums(0, n, m)