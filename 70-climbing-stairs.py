class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n % 2 == 0:
            return 2
        elif n % 2 == 1:
            return 3
