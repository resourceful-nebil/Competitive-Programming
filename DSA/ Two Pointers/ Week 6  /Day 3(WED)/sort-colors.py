class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = -1  # Index for the last position of 0
        one = -1  # Index for the last position of 1
        two = -1  # Index for the last position of 2

        for num in nums:
            if num == 0:
                # Increment the indices and update the values at each position
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
                zero += 1
                nums[zero] = 0
            elif num == 1:
                # Increment the indices and update the values at each position
                two += 1
                nums[two] = 2
                one += 1
                nums[one] = 1
            else:
                # Increment the index and update the value at that position
                two += 1
                nums[two] = 2