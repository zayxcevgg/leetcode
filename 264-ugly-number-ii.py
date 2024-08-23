class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglySet = set()
        uglySet.add(1)

        currUgly = 1
        for iter in range(n):
            currUgly = min(uglySet)
            uglySet.remove(currUgly)
            
            uglySet.add(currUgly * 2)
            uglySet.add(currUgly * 3)
            uglySet.add(currUgly * 5)

        return currUgly

        # if n == 1:
        #     return 1

        # lengthN = n

        # listofTwo = [1]
        # listofThree = []
        # listofFive = []
        # for iter in range(0, n):
        #     listofTwo.append(2 * iter)
        #     listofThree.append(3 * iter)
        #     listofFive.append(5 * iter)
        
        # combinedList = list(set(listofTwo + listofThree + listofFive))

        # return combinedList[n]


      

obj = Solution()
n = 7
obj.nthUglyNumber(n)