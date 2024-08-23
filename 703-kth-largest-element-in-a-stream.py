class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.numsArray = nums
        self.element = -k
        
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.numsArray.append(val)
        self.numsArray.sort()
        #print(self.numsArray[self.element])
        return self.numsArray[self.element]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(3, [4, 5, 8, 2])
# param_1 = obj.add(5)

obj = KthLargest(3, [4, 5, 8, 2]);
obj.add(3);   # return 4
obj.add(5);   # return 5
obj.add(10);  # return 5
obj.add(9);   # return 8
obj.add(4);   # return 8