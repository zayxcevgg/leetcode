from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return''.join(word1) == ''.join(word2)

    word1  = ["abc", "d", "defge"]
    word2 = ["abcddefg"]
    arrayStringsAreEqual(0, word1, word2) 