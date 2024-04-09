class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            team_pass = n%2
            team_play = n // 2
            matches += team_play
            n = team_play + team_pass
        print(matches)
        #if n % 2 == 0:


    n = 7
    numberOfMatches(0, n)