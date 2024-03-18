from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buyPrice, sellPrice = prices[0], prices[0]
#         profit = sellPrice - buyPrice
#         profits = [0]
#         for i in range(1, len(prices)):
#             if buyPrice < prices[i]:
#                 buyPrice, sellPrice = prices[i], prices[i]
#                 profits.append(profit)
#                 profit = sellPrice - buyPrice
#             elif sellPrice < prices[i]:
#                 sell = prices[i]
#                 profit = sell - buyPrice

#         profits.append(profit)
#         print(max(profits))
#         return(max(profits))

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        x = 0 
        for i in prices:
            for j in prices[x:]:
                if j - i > profit:
                    profit = j - i
            x += 1
        print(profit)
            

            
    prices = [7,6,4,3,1]
    maxProfit(0, prices)
