class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)
        stack = 0
        dellater = []
        for i in range(0, len(s)):
            cur_ele = s[i]
            if stack == 0:
                dellater.append(i)
            if s[i] == "(":
                stack += 1
            if s[i] == ")":
                stack -= 1
            if stack == 0:
                dellater.append(i)
        
        dellater = sorted(dellater, reverse=True)
        for j in dellater:
            s.pop(j)
                                  
        return ''.join(s)
    
    s = "(()())(())(()(()))"
    removeOuterParentheses(0, s)