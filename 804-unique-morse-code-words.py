from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique = []
        dict = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        for word in words:
            curr_word = ""
            for letter in word:
                curr_letter = dict[letter]
                curr_word += curr_letter
            if curr_word not in unique:
                unique.append(curr_word)
        
        return len(unique)


    words = ["gin","zen","gig","msg"]
    uniqueMorseRepresentations(0, words)