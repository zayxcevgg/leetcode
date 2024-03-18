class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dict1 = {}
        dict2 = {}

        for x in set(word1):
            dict1[x] = word1.count(x)
            for y in set(word2):
                dict2[y] = word2.count(y)
        list1 = list(dict1.values())
        list1.sort()
        list2 = list(dict2.values())
        list2.sort()
    
        if len(word1) == len(word2) and set(word1) == set(word2) and list1 == list2:
            return True
        else:
            return False
    
    word1 = "abbzzca"
    word2 = "babzzcz"
    closeStrings(0, word1, word2)