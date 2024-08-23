from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        curr = []
        for edge in edges:
            for node in edge:
                if node in curr:
                    return node
                else:
                    curr.append(node)


        return 0
    
    edges = [[1,2],[5,1],[1,3],[1,4]]
    findCenter(0, edges)