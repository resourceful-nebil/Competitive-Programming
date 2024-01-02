class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Initialize two pointers, left and right, pointing to the start and end of the list
        left = 0
        right = len(numbers) - 1
        
        # Initialize an empty list to store the indices of the two numbers that sum up to the target
        ans = []

        # Iterate until the left pointer is less than the right pointer
        while left < right:
            # If the sum of the numbers at the left and right indices is greater than the target,
            # move the right pointer one step to the left
            if numbers[left] + numbers[right] > target:
                right -= 1
            # If the sum of the numbers at the left and right indices is less than the target,
            # move the left pointer one step to the right
            elif numbers[left] + numbers[right] < target: 
                left += 1
            # If the sum of the numbers at the left and right indices is equal to the target,
            # return the indices (adjusted by adding 1 since indices are 1-based)
            else:
                return [left + 1, right + 1]