from collections import defaultdict
from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0  # Initialize the result counter
        di = defaultdict(int)  # Create a defaultdict to store counts
        
        nums.sort()  # Sort the input list
        
        prev = nums[-1]  # Initialize the previous element with the largest element
        di[prev] = 1  # Store the count of the largest element
        
        # If all elements in the list are the same, no operations needed
        if nums.count(nums[0]) == len(nums):
            return 0
        
        # Traverse the sorted list from the second last element to the first
        for i in range(len(nums) - 2, -1, -1):
            # If the current element is the same as the previous element
            if nums[i] == prev:
                di[nums[i]] += 1  # Increment the count of this element
            else:
                # If it's a new element, update its count based on the previous count
                di[nums[i]] = di[prev] + 1
                ans += di[prev]  # Add the count of the previous element to the answer
                prev = nums[i]  # Update the previous element for the next iteration
        
        return ans  # Return the total number of operations
