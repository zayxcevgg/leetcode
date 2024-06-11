from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        i, j = 0, 0
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content_children += 1
                i += 1
            j += 1
        
        return content
    
        for kidgreed in range(len(g)):
            for cookie in range(len(s)):
                if s[cookie] >= abs(g[kidgreed]):
                    content.append(g[kidgreed])
                    g[kidgreed] = -999999999
                    s[cookie] = -99999999
                        # s.remove(kidgreed)


        print(len(content))
        return len(content)

        #g.remove(content)
    g = [10,9,8,7]
    s = [5,6,7,8]
    findContentChildren(0, g, s)