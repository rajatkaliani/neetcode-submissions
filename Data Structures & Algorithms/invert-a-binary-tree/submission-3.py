# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(rootnode):
            if not rootnode:
                return None
            temp = rootnode.right
            rootnode.right = rootnode.left
            rootnode.left = temp
            dfs(rootnode.left)
            dfs(rootnode.right)
        dfs(root)
        return root


