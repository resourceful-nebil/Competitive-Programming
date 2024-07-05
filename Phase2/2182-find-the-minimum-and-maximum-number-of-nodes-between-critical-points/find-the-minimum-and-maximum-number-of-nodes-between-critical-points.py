# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev_node, curr_node = head, head.next
      
        first_critical, last_critical = None, None
      
        index = 1  
        min_distance, max_distance = inf, -inf  
      
        while curr_node.next:
            if curr_node.val < min(prev_node.val, curr_node.next.val) or \
               curr_node.val > max(prev_node.val, curr_node.next.val):
                if last_critical is None:
                    first_critical = last_critical = index
                else:
                    min_distance = min(min_distance, index - last_critical)
                    max_distance = index - first_critical
                    last_critical = index
            index += 1
            prev_node, curr_node = curr_node, curr_node.next
      
        return [min_distance, max_distance] if first_critical != last_critical else [-1, -1]