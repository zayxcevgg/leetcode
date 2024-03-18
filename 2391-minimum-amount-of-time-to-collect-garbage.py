from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        truckG = 0
        truckP = 0
        truckM = 0
        dist = [0, 0, 0] # G, P, M
       
        for house in range(0, len(garbage)):
            if garbage[house].count("G"):
                truckG += garbage[house].count("G")
                dist[0] = house

            if garbage[house].count("P"):
                truckP += garbage[house].count("P")
                dist[1] = house

            if garbage[house].count("M"):
                truckM += garbage[house].count("M")
                dist[2] = house

        truckG += sum(travel[:dist[0]])
        truckP += sum(travel[:dist[1]])
        truckM += sum(travel[:dist[2]])

        return truckG + truckP + truckM    

    garbage = ["MMM","PGM","GP"]
    travel = [3,10]
    garbageCollection(0, garbage, travel)