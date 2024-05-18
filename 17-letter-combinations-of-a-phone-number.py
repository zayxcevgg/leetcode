from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }
        options = []
        for i in digits:
            answers = keyboard[i]
            for x, y in enumerate(answers):
                options[x] = y


    digits = "23"
    letterCombinations(0, digits)