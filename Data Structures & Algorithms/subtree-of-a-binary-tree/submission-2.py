# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.trav = ""
        def dfs(node):
            if node is None:
                self.trav += "#"
                return
            self.trav+= str(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        bigger = self.trav
        print(self.trav)
        self.trav = ""
        dfs(subRoot)
        print(self.trav)
        smaller = self.trav
        return (smaller in bigger)

