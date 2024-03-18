class Solution:
    def isPalindrome(self, x: int) -> bool:
        for i in range (0, len(str(x))):
            #print(len(str(x)),str(x)[i], str(x)[len(str(x))-i-1])
            if str(x)[i] != str(x)[len(str(x))-i-1]:
                res = False
                break
            else:
                res = True
        print(x, res)
        return res

    isPalindrome(0, 1000021)
    isPalindrome(0, -121)
    isPalindrome(0, 10)