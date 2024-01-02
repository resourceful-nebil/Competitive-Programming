class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize a variable 'holder' to keep track of the position where non-zero elements should be placed
        holder = 0

        # Iterate through the 'nums' list
        for i in range(len(nums)):
            # If the current element is not zero
            if nums[i] != 0:
                # Swap the current element with the element at the 'holder' position
                nums[i], nums[holder] = nums[holder], nums[i]
                # Increment 'holder' by 1 to maintain its position for the next non-zero element
                holder += 1