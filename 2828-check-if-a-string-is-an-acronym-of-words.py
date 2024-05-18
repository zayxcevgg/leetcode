from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letters = ""
        for word in words:
            letters += word[:1]

        return s == letters

    words = ["alice","bob","charlie"]
    s = "abc"
    isAcronym(0, words, s)