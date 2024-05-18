class Solution:
    def minPartitions(self, n: str) -> int:
        numbers = 0
        n = int(n)
        while n > 10:
            if n % 10 == 0:
                numbers += n // 10
                n = n / 10
            else:
                n = n - 11
                numbers += 1
        print(numbers)

    n = "32"
    minPartitions(0, n)

