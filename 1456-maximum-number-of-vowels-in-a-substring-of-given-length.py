class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        if k > n:
            return -1
        vowels = {'a', 'e', 'i', 'o', 'u'}


        win_count = 0
        for i in range(k):
            win_count += int(s[i] in vowels)
        max_count = win_count

        for j in range(k, n):
            win_count += int(s[j] in vowels)
            win_count -= int(s[j - k] in vowels)
            max_count = max(max_count, win_count)

        print(max_count)
        return max_count


        
    
    s = "abciiidef"
    k = 3
    maxVowels(0, s, k)