# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head

        curr_odd = head
        curr_even = head.next

        even = ListNode()
        odd = ListNode()

        odd.next = curr_odd
        even.next = curr_even

        while curr_odd and curr_odd.next and curr_even and curr_even.next:
            curr_odd.next = curr_odd.next.next
            curr_even.next = curr_even.next.next
            curr_odd = curr_odd.next
            curr_even = curr_odd.next

        curr_odd.next = even.next

        return odd.next
           


            

            

        