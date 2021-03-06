# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _dfs(self, node, target):
        if node: 
            if node.val==target.val:
                return node
            return Solution._dfs(self, node.left, target) or Solution._dfs(self, node.right, target)
            
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return Solution._dfs(self, cloned, target)

"""
This works simply enough. Recursively call on node: if None return None, if it's target return itself, otherwise recursivley call on left and right. That return statement works because of the "or" which conveniently returns the first non-None operand or None if they're both None. 

--Problems--
Unfortunely for this solution, it runs on all nodes of the tree. Also, it cannot handle duplicate values. 

"""

