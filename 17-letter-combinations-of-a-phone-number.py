from typing import List
import itertools

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
        
        usedLetters = []  
        for digit in digits:
            usedLetters.append(list(keyboard[digit]))
        print(usedLetters)

        for usedKey in range(usedLetters):
            for j in usedKey:
                print(usedLetters[usedKey][j])
            
               #
        


                    
        #return result
        
        #return list(itertools.product(*usedLetters))


    


obj = Solution()
digits = "23"
obj.letterCombinations(digits)