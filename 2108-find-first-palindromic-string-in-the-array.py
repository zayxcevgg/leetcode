from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
            else:
                continue
                
    words = ["abc","car","ada","racecar","cool"]
    firstPalindrome(0, words)