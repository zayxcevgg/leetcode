class Solution:
    def countAsterisks(self, s: str) -> int:
        toggle = True
        count = 0
        for i in s:
            if i == "|":
                toggle = not toggle
            
            if i == "*" and toggle == True:
                count += 1

        print(count)

    s = "l|*e*et|c**o|*de|"
    countAsterisks(0, s)