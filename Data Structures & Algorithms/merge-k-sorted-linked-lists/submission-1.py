# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        i = 0
        for node in lists:
            heapq.heappush(heap,(node.val,i,node))
            i = i + 1
        if not heap:
            return None

        chain = ListNode((0,0,None))
        head = chain
        while heap:
            srt = heapq.heappop(heap)[2]
            chain.next = srt
            chain = chain.next
            if srt.next:
                heapq.heappush(heap,(srt.next.val,i,srt.next))
                i = i + 1
        return head.next
