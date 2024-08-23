class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return round(s.count(letter) / len(s) * 100)

    s = "foobar"
    letter = "o"
    percentageLetter(0, s, letter)