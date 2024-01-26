# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left , right = ListNode() , ListNode()
        ltmp,rtmp = left,right

        while head:
            if head.val < x:
                ltmp.next = head
                ltmp = ltmp.next
            else:
                rtmp.next = head
                rtmp = rtmp.next
        
            head = head.next
        
        ltmp.next = right.next
        rtmp.next = None

        return left.next
