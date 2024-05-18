class Solution:
    def replaceDigits(self, s: str) -> str:
        l = list(s)
        for i, j  in enumerate(s):
            if j.isalpha() or int(j) % 2 == 0:
                pass
            else:
                l[i] = chr(ord(s[i - 1]) + int(s[i])) # ? conv to ascii vals and add up

        print(''.join(l))


    s = "a1c1e1"
    replaceDigits(0, s)