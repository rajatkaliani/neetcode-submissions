# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        temp = head
        if (not head):
            return False
        while (temp.next != None):
            val = temp.val
            if val in seen:
                return True
            seen.add(val)
            temp = temp.next
        return False

        