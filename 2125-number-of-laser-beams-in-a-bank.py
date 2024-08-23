from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams_list = []
        for row in bank:
            if "1" in row:
                beams_list.append(row.count("1"))
        total_beams = 0

        for beam in range(0, len(beams_list) - 1):
            total_beams += beams_list[beam] * beams_list[beam + 1]
    
        return total_beams
    
    bank = ["011001","000000","010100","001000"]
    numberOfBeams(0, bank)
