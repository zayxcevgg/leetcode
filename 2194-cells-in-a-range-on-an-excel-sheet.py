from typing import List
import re

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
            alphabetUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            split_cells = re.split('(\d+)', s.replace(':', ''))
            
            start_col_letter = split_cells[0]
            start_row_number = int(split_cells[1])
            end_col_letter = split_cells[2]
            end_row_number = int(split_cells[3])

            result_cells = []

            for col_letter in range(ord(start_col_letter), ord(end_col_letter) + 1):
                for row in range(start_row_number, end_row_number + 1):
                    result_cells.append(f"{chr(col_letter)}{row}")

            return result_cells
            


    s = "A12:K21"
    cellsInRange(0, s)