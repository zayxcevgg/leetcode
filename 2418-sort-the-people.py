from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_dict = dict(zip(heights, names))
        heights_dict = sorted(heights_dict.items(), reverse=True)
        res_names = [name for height, name in heights_dict]

        return res_names
    
    names = ["IEO","Sgizfdfrims","QTASHKQ","Vk","RPJOFYZUBFSIYp","EPCFFt","VOYGWWNCf","WSpmqvb"]
    heights = [17233,32521,14087,42738,46669,65662,43204,8224]

    sortPeople(0, names, heights)