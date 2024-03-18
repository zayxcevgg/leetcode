class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        dict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4: "IV", 1:"I"}
        for i in dict.keys():
            while i <= num:
                roman += dict[i]
                num-=i
        print(roman)
                
    num = 1994
    intToRoman(0, num)