from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in accounts:
            wealth = sum(i)
            print(accounts, wealth)
            if maxWealth < wealth:
                maxWealth = wealth
        
        print(maxWealth)
        return maxWealth

    maximumWealth(0, [[2,3,4],[1,1,1]])