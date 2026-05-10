# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.trav = []
        def dfs(node):
            if node is None:
                self.trav.append(-1)
                return
            self.trav.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(p)
        left = self.trav
        print("Left:" + str(self.trav))
        self.trav = []
        dfs(q)
        print("Right:" + str(self.trav))
        right = self.trav
        return right == left