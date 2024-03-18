import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[,:.@#_!'\\\{\}\"\"\[\]\-?;\(\)1234567890\` ]","", s).lower()
        print(s)  
    s = "0P"
    isPalindrome(0, s)