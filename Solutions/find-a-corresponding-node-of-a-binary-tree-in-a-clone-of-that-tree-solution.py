# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def _bfs(self, node, target):
        if node is None: 
            return None
        if node.val==target.val:
            return node
        return Solution._bfs(self, node.left, target) or Solution._bfs(self, node.right, target)
            
    
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return Solution._bfs(self, cloned, target)



