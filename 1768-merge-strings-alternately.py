class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            i += 1

        print(''.join(map(str, merged)))
        return ''.join(map(str, merged))
    
    word1 = "abc"
    word2 = "pqr"
    mergeAlternately(0, word1, word2)