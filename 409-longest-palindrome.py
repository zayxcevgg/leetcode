class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        sum = 0
        odd_found = False

        for count in letters.values():
            if count % 2 == 0:
                sum += count
            else:
                sum += count - 1
                odd_found = True
        
        if odd_found:
            sum += 1
        #return


        print(sum)

    s = "bbgfdvvvvsafweaggaghgh"
    longestPalindrome(0, s)