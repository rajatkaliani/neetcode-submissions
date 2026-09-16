# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            val = None
            for i in range(len(queue)):
                processing = queue.popleft()
                if val == None:
                    val = processing.val
                if processing.right:
                    queue.append(processing.right)
                if processing.left:
                    queue.append(processing.left)
            res.append(val)
        return res

        