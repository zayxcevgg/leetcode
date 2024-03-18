from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number  = int(''.join(map(str, digits))) + 1 
        return [int(digit) for digit in str(number)]

    digits = [9]
    plusOne(0, digits)