# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(rootnode):
            if (rootnode == None):
                return None
            tmp = rootnode.left
            rootnode.left = rootnode.right
            rootnode.right = tmp

            self.invertTree(rootnode.left)
            self.invertTree(rootnode.right)
            return rootnode
        return dfs(root)

