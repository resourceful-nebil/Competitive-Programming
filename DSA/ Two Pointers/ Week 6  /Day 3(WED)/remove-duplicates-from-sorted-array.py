class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer j to keep track of the new length of the array
        j = 1
        
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous element
            if nums[i] != nums[i - 1]:
                # If the current element is different, update the value at index j with the current element
                nums[j] = nums[i]
                # Increment j to move to the next position for the next unique element
                j += 1
        
        # Return the new length of the array, represented by j
        return j