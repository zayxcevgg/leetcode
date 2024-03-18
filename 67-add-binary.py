class Solution:
    def addBinary(self, a: str, b: str) -> str:
        print(str(bin(int(a, 2) + int(b, 2)))[2:])
        return bin(int(a, 2) + int(b, 2))[2:]
    
    a = "11"
    b = "1"
    addBinary(0, a, b)