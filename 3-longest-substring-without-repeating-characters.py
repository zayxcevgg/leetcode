class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = {}
        longest = 0
        counter = 0
        for i in s:
            if i not in uniq:
                counter += 1
                uniq[i] = counter
            else:
                #uniq.del(uniq[i])
                uniq[i] = 1
                counter = 1
            longest = max(longest, uniq[i])

        print(longest)
        return longest
    

    string ="dvdf"
    lengthOfLongestSubstring(0, string)
        