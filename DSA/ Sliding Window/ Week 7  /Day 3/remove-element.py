class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize two pointers, l and r, both pointing to the start of the array
        l, r = 0, 0
        
        # Iterate through the array
        while r < len(nums):
            # If the current element is not equal to the target value
            if nums[r] != val:
                # Move the current element to the left side of the array
                nums[l] = nums[r]
                # Increment the left pointer to mark the next position to be replaced
                l += 1
            # Move the right pointer to the next element in the array
            r += 1
    
        # Return the length of the array up to the left pointer, which represents the new length
        return len(nums[:l])