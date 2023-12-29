class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        # Convert integers to strings
        nums = list(map(str, nums))

        # Bubble sort implementation based on custom comparison function
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Comparing concatenation of two numbers in two different orders
                # If concatenation of nums[i] + nums[j] is smaller than nums[j] + nums[i],
                # it means nums[i] should come before nums[j] in order to form a larger number
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    # Swap the positions of the numbers to form the larger number
                    nums[j], nums[i] = nums[i], nums[j]
        
        # Join the sorted numbers into a single string and convert it back to an integer
        # Then convert the integer back to a string and return
        return str(int("".join(nums)))
