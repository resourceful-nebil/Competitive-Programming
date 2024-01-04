class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Sort the input list to use two pointers for comparisons
        nums.sort() 
        
        # Initialize the count of operations
        op = 0
        
        # Initialize two pointers for comparison: one from the start and the other from the end
        i = 0
        j = len(nums) - 1

        # Loop until the pointers meet or cross
        while i < j:
            # If the sum of elements at pointers matches the target 'k'
            if nums[i] + nums[j] == k:
                # Increment the operation count
                op += 1
                
                # Move both pointers inward to check for other pairs
                i += 1
                j -= 1
                
            # If the sum is greater than the target 'k'
            elif nums[i] + nums[j] > k:
                # Decrement the 'j' pointer to decrease the sum
                j -= 1
            
            # If the sum is less than the target 'k'
            else:
                # Increment the 'i' pointer to increase the sum
                i += 1
        
        # Return the count of valid operations
        return op
