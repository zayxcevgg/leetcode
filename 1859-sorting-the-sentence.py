class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(' ')
        res = [0] * len(l)
        for i in l:
            res[int(i[-1]) - 1] = i[:-1]
        
        return ' '.join(res)

    s = "Myself2 Me1 I4 and3"
    sortSentence(0, s)