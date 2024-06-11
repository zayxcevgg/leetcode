from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dictionary = {}
        for i in range(len(arr1)):
            if arr1[i] in dictionary:
                dictionary[arr1[i]] += 1
            else:
                dictionary[arr1[i]] = 1

        reslist = []
        leftover = []
        for j in arr2:
            sublist = [j] * dictionary.get(j)
            reslist += sublist
            counter = 0
            while counter < dictionary.get(j):
                arr1.remove(j)
                counter += 1
        reslist += sorted(arr1)

        return reslist
        print(reslist, arr1)
        return 0


    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    relativeSortArray(0, arr1, arr2)