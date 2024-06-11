from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counter = 0
        while len(hand) >= groupSize:
            inHand = []
            for j in range(0, groupSize):
                if hand[0] + j in hand:
                    inHand.append(hand[0] + j)
                else:
                    return False
            counter +=1
            for e in inHand:
                hand.remove(e)
                
        return True
    
    hand = [8,8,9,7,7,7,6,7,10,6]
    groupSize = 2
    isNStraightHand(0, hand, groupSize)