# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while head != None:
            count = count + 1
            head = head.next
        head = temp
        if (count == 1):
            return None
        if (count == n):
            return head.next
        for i in range(count-1):
            print(i)
            if i+1 == count-n:
                head.next = head.next.next
            head = head.next
        return temp


