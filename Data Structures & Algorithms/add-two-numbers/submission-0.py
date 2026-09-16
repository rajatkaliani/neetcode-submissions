# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1val = 0
        l2val = 0
        i = 0
        while l1:
            l1val += ((10**i)*l1.val)
            i = i +1
            l1 = l1.next
        j = 0
        while l2:
            l2val += (10**j)*l2.val
            j = j + 1
            l2 = l2.next
        sumi = str(l1val+l2val)
        resNode = ListNode(sumi[-1])
        print(sumi)
        ret = resNode
        for i in range(1,len(sumi)):
            resNode.next = ListNode(sumi[len(sumi)-i-1])
            resNode = resNode.next
        return ret

    

