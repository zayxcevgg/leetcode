from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxI = 0
        for i in sentences:
            length = i.split()
            maxI = max(maxI, len(length))

        return maxI
        



    sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
    mostWordsFound(0, sentences)