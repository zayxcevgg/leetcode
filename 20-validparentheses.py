class Solution:
    def isValid(self, s: str) -> bool:
        balance = ""
        for i in s:
            if i == "{" or i == "(" or i == "[":
                balance = balance + i
            elif i == "}" or i == ")" or i == "]":
                balance = balance - i
            print(balance)
            
        if balance != 0:
            return False
        else:
            return True

    isValid(0, "(]")