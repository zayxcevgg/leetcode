class Solution:
    def maxDepth(self, s: str) -> int:
        level = 0
        max_level = 0
        for i in s:
            if i == '(':
                level += 1
            if i == ')':
                level -= 1
            if max_level < level:
                max_level = level
        
        return max_level

    s = "(1+(2*3)+((8)/4))+1"
    maxDepth(0, s)

            