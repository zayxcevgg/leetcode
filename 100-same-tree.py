from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            print("T")
            return True
        
        if not p or not q:
            print("T")
            return False
        
        if str(p.val) != str(q.val):
            print("F")
            return False
        
        print(self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    p = TreeNode[1,2,3]
    q = TreeNode[1,2,3]
    isSameTree(0, p, q)