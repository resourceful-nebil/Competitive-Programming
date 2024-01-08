class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize two pointers, `left` and `right`, to track the window boundaries.
        left, right = 0, 0
        # Initialize a variable to keep track of the maximum number of consecutive ones encountered so far.
        max_ones = 0
        # Initialize a variable to keep track of the number of zeros encountered within the window.
        zero_count = 0

        while right < len(nums):
            # If the element at `right` is 0, increment `zero_count` by 1.
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                # If the element at `left` is 0, decrement `zero_count` by 1.
                if nums[left] == 0:
                    zero_count -= 1
                # Increment `left` to shrink the window from the left side.
                left += 1

            # Update `max_ones` to be the maximum of `max_ones` and the length of the current window (consecutive ones plus `k` flipped zeros).
            max_ones = max(max_ones, right - left + 1)

            # Move the `right` pointer forward.
            right += 1

        return max_ones