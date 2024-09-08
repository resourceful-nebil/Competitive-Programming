# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head

        # to get the length of the linked list
        while curr:
            curr = curr.next
            length += 1

        base_len, remainder = length // k, length % k
        curr = head
        res= []
        for i in range(k):
            res.append(curr)

            end_value = base_len - 1
            if remainder:
                end_value += 1

            for j in range(end_value):
                if not curr: 
                    break
                curr = curr.next 
            if remainder > 0:
                remainder -= 1
            if curr:
                curr.next,curr = None, curr.next
        
        return res



        