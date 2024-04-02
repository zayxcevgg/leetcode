class Solution:
    def numberOfSteps(self, num: int) -> int:
        loops = 0
        while num != 0:
            loops += 1
            if num % 2 == 0:
                num = num/2
            else:
                num -= 1
        return loops
    
    numberOfSteps(0, 14)
    