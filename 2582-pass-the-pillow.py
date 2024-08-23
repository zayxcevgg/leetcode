class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person = 1
        reverse = False
        while time != 0:
            if person == n and reverse == False:
                reverse = True

            if person == 1 and reverse == True:
                reverse = False

            if reverse == True:
                person -= 1
            else:
                person += 1
            time -= 1

        return person
    
    n = 3
    time = 2
    passThePillow(0, n, time)