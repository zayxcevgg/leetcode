from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res_arr = []
        for w in range(len(words)):
            if x in words[w]:
                res_arr.append(w)
        return res_arr
        

    words = ["abc","bcd","aaaa","cbc"]
    x = "a"
    findWordsContaining(0, words, x)


    # results=[]
    #     for w in range(len(words)):
    #         if x in words[w]:
    #             results.append(w)
    #     return results