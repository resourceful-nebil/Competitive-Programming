# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_sum = 0
        dummy = ListNode(0)
        dummy_temp = dummy

        temp = head.next
        while temp:
            cur_sum += temp.val
            if temp.val == 0:
                dummy_temp.next = ListNode(cur_sum)
                cur_sum = 0
                dummy_temp = dummy_temp.next
            
            temp = temp.next
        return dummy.next


