# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append(root)
        res = []
        while queue:
            level = []
            for i in range(len(queue)):
                bob = queue.popleft()
                level.append(bob.val)
                if bob.left:
                    queue.append(bob.left)
                if bob.right:
                    queue.append(bob.right)
            res.append(level)
        return res
        