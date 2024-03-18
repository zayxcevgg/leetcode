from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        for i in graph:
            if not i:
                pass
            else:
                print(i)

    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    eventualSafeNodes(0, graph)