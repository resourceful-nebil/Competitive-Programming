class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input list for easier traversal
        nums.sort()
        
        # Initialize variables to keep track of the minimum difference ('mi') and the sum closest to the target ('total')
        mi = float('inf')  # Initialize 'mi' with positive infinity to ensure it gets updated in the loop
        total = 0  # Initialize the 'total' sum
        
        # Loop through the sorted list for the first element
        for i in range(len(nums)-2):  # Loop until the third last element
            j = i + 1  # Pointer for the second element of the triplet
            k = len(nums) - 1  # Pointer for the third element of the triplet
            
            # While the two pointers don't cross each other
            while j < k:
                # Calculate the sum of the three elements
                add = nums[i] + nums[j] + nums[k]
                
                # Check if the absolute difference between the current sum and the target is smaller than 'mi'
                if mi > abs(target - add):
                    mi = abs(target - add)  # Update 'mi' to the new minimum difference
                    total = add  # Update 'total' to the sum closest to the target
                
                # Adjust the pointers based on the comparison with the target
                if add < target:
                    j += 1  # If the sum is less than the target, move the 'j' pointer to increase the sum
                else:
                    k -= 1  # If the sum is greater than the target, move the 'k' pointer to decrease the sum
        
        # Return the sum that is closest to the target
        return total
