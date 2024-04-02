class Solution:
    def isValid(self, s: str) -> bool:
        round = 0
        square = 0
        sharp = 0

        for i in s: 
            if i == "{" 
            elif i == "(" elif i == "[":
                balance = balance + i
            elif i == "}" or i == ")" or i == "]":
                balance = balance - i
            print(balance)
            
        if balance != 0:
            return False
        else:
            return True

    isValid(0, "(]")