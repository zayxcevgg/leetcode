class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        strUniq =''.join(set(sentence))
        if len(strUniq) == 26:
            return True
        return False

    
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    checkIfPangram(0, sentence)