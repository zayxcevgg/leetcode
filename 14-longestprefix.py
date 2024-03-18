from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        
        for i in strs:
            while len(shortest) > 0:
                if i.startswith(shortest):
                    break
                else:
                    shortest = shortest[:-1] 
        return shortest
    
    longestCommonPrefix(0, ["a"])
       
        # prefix = strs[0]
        # for i in range(len(prefix)):
        #     for word in strs[1:]:
        #         if (i == len(word) or word[i] != prefix[i]):
        #             return prefix[0:i]
    
                
        #         for j in range(1, len(strs)):
        #             if strs[0][i] != strs[j][i]:
        #                 quit                      
        #         print(strs[0][i])
        #         prefix = prefix + strs[0][i]
        # except IndexError:
        #     print(prefix)
        #     return prefix
        
        # for word in strs[1:]:
        #         if (i == len(word) or word[i] != base[i]):
        #     #
        #     # for j in i:
              #  print(str(j))
            
     #       for j in enumerate(strs):
    #             if strs[0][i] == strs[j][i]:
    #                 pass
    #             else:
    #                 return ""
    #                 break
    #         prefix = prefix + strs[i][j]
    #     return prefix
   