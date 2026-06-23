# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recurse(node):
            if node.val > p.val and node.val > q.val:
                print(node.left.val)
                return recurse(node.left)
            elif node.val < p.val and node.val < q.val:
                print(node.right.val)
                return recurse(node.right)
            else:
                return node
        return recurse(root)

