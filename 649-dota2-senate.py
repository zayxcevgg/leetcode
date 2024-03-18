from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiantAct = deque()
        direAct =  deque()
        for i in range(0, len(senate)):
            if senate[i] == "R":
                radiantAct.append(i)
            else:
                direAct.append(i)
        j = 0
        while radiantAct and direAct:
            if radiantAct[0] < direAct[0]:
                direAct.popleft()
                radiantAct.append(radiantAct[0] + 100)
                radiantAct.popleft()
            else:
                radiantAct.popleft()
                direAct.append(direAct[0] + 100)
                direAct.popleft()

        if len(direAct) == 0:
            print("Radiant")
        else:
            print("Dire")
                
    senate = "DRRDRDRDRDDRDRDRD"
    predictPartyVictory(0, senate)