class Solution:
    def reverseVowels(self, s: str) -> str:
        
        order = []
        vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s:
            if i in vovels:
                order.append(i)
        
        order.reverse()

        resword = ''
        for j in range(0, len(s)):
            if s[j] in vovels:
                resword =  resword + order[0]
                order.pop(0)
            else:
                resword =  resword + s[j]

        return resword
        
    s = "leetcode"       
    reverseVowels(0, s)
