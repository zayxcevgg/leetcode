class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])
        
    s = "Hello how are you Contestant"
    k = 4
    truncateSentence(0, s, k)