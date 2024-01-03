class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # Initialize count variable to keep track of the number of pairs
        count = 0
        
        # Iterate over each element in the list
        for i in range(len(nums)):
            # Iterate over remaining elements in the list
            for j in range(i + 1, len(nums)):
                # Check if the sum of the current pair is less than the target
                if nums[i] + nums[j] < target:
                    count += 1  # If the sum is less than the target, increment the count
        
        return count  # Return the count of pairs