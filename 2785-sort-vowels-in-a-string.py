class Solution:
    def sortVowels(self, s: str) -> str:
        l = list(s)
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        mixVovels = []

        for i, j in enumerate(l):
            if j in vowels:
                mixVovels.append(j)
                l[i] = "*"

        srtVovels = sorted(mixVovels, key = lambda s: sum(map(ord, s)), reverse=False)

        for x, y in enumerate(l):
            if y == "*":
                l[x] = srtVovels[0]
                srtVovels.pop(0)

        return ''.join(l)



    s = "lEetcOde"
    sortVowels(0, s)