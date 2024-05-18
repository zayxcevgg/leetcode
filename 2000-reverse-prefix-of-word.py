class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            pref = word.index(ch)
            print(word[0:pref+1][::-1] + word[pref:])
            return word[0:pref+1][::-1] + word[pref:]
        except:
            print(word)
            return word



    word = "abcdefd"
    ch = "d"
    reversePrefix(0, word, ch)