from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
            dp = {}
            result = 0 

            for num in arr:
                if num - difference in dp:
                    dp[num] = dp[num - difference] + 1 # ne ponel kak rabotaet
                else:
                    dp[num] = 1
                result = max(result, dp[num])

            print(result)
            return result


    arr1 = [1,2,3,4]
    arr2 = [1,3,5,7]
    arr3 = [1,5,7,8,5,3,4,2,1]
    arr4 = [3,0,-3,4,-4,7,6]
    arr5 = [6,-2,0,3,-7,6,-5,-8]
    difference1 = 1
    difference2 = -2
    difference3 = 3
    difference5 = -5
    #longestSubsequence(0, arr1, difference1)
    #longestSubsequence(0, arr2, difference1)
    longestSubsequence(0, arr3, difference2)
    #longestSubsequence(0, arr4, difference3)
    #longestSubsequence(0, arr5, difference5)
