# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count = count + 1
            temp = temp.next
        if count == n:
            return head.next
        p = None
        h = head
        print(count-n)
        for _ in range(count-n):
            if head.next:
                p = h
                h = h.next

        p.next = h.next
        return head
        


