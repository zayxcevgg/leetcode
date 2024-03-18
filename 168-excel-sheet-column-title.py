class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        second = columnNumber % 26 - 1
        first = int(columnNumber / 26) - 1

        if first >= 0 and second >= 0:
            return alpha[first] + alpha[second]
        else:
            return alpha[second]
            

    columnNumber = 2147483647
    convertToTitle(0, columnNumber)