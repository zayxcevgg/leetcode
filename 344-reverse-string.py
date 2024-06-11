from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)//2):
            temp_var = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp_var

            print(s)



    s = ["H","a","n","n","a","h"]
    reverseString(0, s)