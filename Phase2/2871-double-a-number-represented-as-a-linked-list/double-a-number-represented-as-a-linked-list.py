# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Helper function to reverse the linked list.
        def reverse(node):
            dummy = ListNode()
            current = node
            while current:
                next_node = current.next
                current.next = dummy.next
                dummy.next = current
                current = next_node
            return dummy.next
      
        # Step 1: Reverse the input list to make it easier to double the digits from the least significant digit.
        head = reverse(head)
      
        # Initialize a new dummy head for the result list.
        dummy = current = ListNode()
        multiplier = 2  # The factor by which we want to multiply each node's value.
        carry = 0  # Initialize the carry for multiplication.
      
        # Step 2: Traverse the reversed list, doubling each digit and managing the carry.
        while head:
            product = head.val * multiplier + carry  # Multiply the current value and add the carry.
            carry = product // 10  # Update carry for the next iteration.
            current.next = ListNode(product % 10)  # Create a new node with the single digit.
            current = current.next  # Move to the next position in the result list.
            head = head.next  # Move to the next node in the input list.
      
        # Step 3: If there is a carry left after the loop, add it as a new node.
        if carry:
            current.next = ListNode(carry)
      
        # Step 4: Reverse the result list back to original order and return.
        return reverse(dummy.next)