from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # charsdict = {}
        # for word in words:
        #     for letter in word:
        #         if letter in charsdict:
        #             charsdict[letter] += 1
        #         else:
        #             charsdict[letter] = 1

        # res = []
        # for chard in charsdict:
        #     if charsdict.get(chard) >= len(words):
        #         if charsdict.get(chard) == len(words):
        #             res.append(str(chard))
        #         else:
        #             while charsdict.get(chard) >= len(words):
        #                 charsdict[chard] = int(charsdict.get(chard)) - len(words)
        #                 res.append(chard)

        # return res
        checkword = {}
        
        for letter in words[0]:
            if letter in checkword:
                checkword[letter] += 1
            else:
                checkword[letter] = 1
        
        
        for word in words[1:]:
            currword = {}
            for letter in word:
                if letter in currword:
                    currword[letter] += 1
                else:
                    currword[letter] = 1

            letters_to_remove = []
            for letter in checkword:
                if letter in currword:
                    checkword[letter] = min(checkword[letter], currword[letter])
                else:
                    letters_to_remove.append(letter)

            for letter in letters_to_remove:
                del checkword[letter]

        result = []
        for letter, count in checkword.items():
            if count != '!':
                result.extend([letter] * count)

        return result

        # for charsletter in range(len(charsDict)):
        #         if charsDict[charsletter] not in word:
        #             print("removed " + charsDict[charsletter] + " not in word " + word)
        #             charsDict[charsletter] = "!"
        #             continue
        #         continue
        
        # return [i for i in charsDict if i != "!"]
        

    words = ["bella","label","roller"]
    #words = ["cool","lock","cook"]
    #words = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
    commonChars(0, words)

    