from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0
        uniq = []
        for i in range(0, len(words)):
            word = words[i]
            words[i] = '00'
            revword = word[::-1]
            if words.count(revword) > 0 and word not in uniq:
                counter += 1
            uniq.append(word)
            uniq.append(revword)

        return counter
    
    words = ["cd","ac","dc","ca","zz"]
    maximumNumberOfStringPairs(0, words)