class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute the initial sum of the first k elements
        window_sum = sum(nums[:k])

        # Set the initial maximum average to the window sum
        max_average = window_sum

        # Slide the window over the array and update the maximum average
        for i in range(k, len(nums)):
            # Update the window sum by subtracting the element going out of the window
            # and adding the element coming into the window
            window_sum = window_sum + nums[i] - nums[i - k]

            # Update the maximum average if the current window sum is greater
            max_average = max(window_sum, max_average)

        # Return the maximum average by dividing the max_average by k
        return max_average / k