from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        print(altitudes, max(altitudes))
        return max(altitudes)

    gain = [-4,-3,-2,-1,4,3,2]
    largestAltitude(0, gain)
            