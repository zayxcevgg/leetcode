class Solution(object):
    @staticmethod
    def digitEng(self, triplet):
        d = {0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"
        }
        if len(triplet) == 1: # 1
            ones = d[int(triplet[0])]
            result = ones

        elif len(triplet) == 2: # 20 
            tens = d[int(triplet[0] + "0")]
            if int(triplet[1]) != 0:
                ones = d[int(triplet[1])]
            else:
                ones = ''

            if int(triplet[0]) == 1:
                tens = d[int(triplet)]
                result = tens
            else:
                result = tens + " " + ones

        else:  # 313
            if int(triplet[0]) == 0:
                hundreds = ''
            else:
                hundreds = d[int(triplet[0])] + " Hundred"
            
            if int(triplet[1]) == 0:
                tens = ''
            else:
                tens = d[int(triplet[1] + "0")]
            
            if int(triplet[1]) == 1:
                tens = d[int(triplet[1:])]
                triplet = triplet[1:] + '0'

            if int(triplet[2]) == 0:
                ones = ''
            else:
                ones = d[int(triplet[2])]
            result = ''
            for iter in [hundreds, tens, ones]:
                if iter:
                    result += " "  + iter
            # elif not tens: result = hundreds + " " + ones
            # elif not ones: result = hundreds + " " + tens
            # else: result = hundreds + " " + tens + " " + ones


        return result.strip()
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = str(num)
        digits = len(num)
        if digits > 9:
            billions = num[:digits-9]
            millions = num[digits-9:digits-6]
            thousands = num[digits-6:digits-3]
            hundreds = num[digits-3:]
        elif digits > 6:
            billions = ""
            millions = num[:digits-6]
            thousands = num[digits-6:digits-3]
            hundreds = num[digits-3:digits]
        elif digits > 3:
            billions = ""
            millions = ""
            thousands = num[:digits-3]
            hundreds = num[digits-3:digits]
        else:
            billions = ""
            millions = ""
            thousands = ""
            hundreds = num

        
        english = ""
        if billions: english += Solution.digitEng(0, billions) + " Billion "
        if millions: english += Solution.digitEng(0, millions) + " Million "
        if thousands and thousands != '000': english += Solution.digitEng(0, thousands) + " Thousand "
        if hundreds:english += Solution.digitEng(0, hundreds)

        print(english)
        return english.strip()
    

sol = Solution()
sol.numberToWords(101)
