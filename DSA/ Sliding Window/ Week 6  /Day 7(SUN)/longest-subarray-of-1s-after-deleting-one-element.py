class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize two pointers
        l, r = 0, 0
        # Initialize a variable to keep track of the maximum length of the subarray.
        max_length = 0
        # Initialize a variable to keep track of the number of zeroes encountered within the window.
        count_zeroes = 0

        while r < len(nums):  
            # If the element at `r` is 0, increment `count_zeroes` by 1.
            if nums[r] == 0:  
                count_zeroes += 1

            # If `count_zeroes` becomes 2 (indicating we have encountered more than one zero within the window):
            while count_zeroes > 1:  
                # Move the `l` pointer forward until we remove the leftmost zero from the window.
                if nums[l] == 0:  
                    count_zeroes -= 1
                l += 1

            # Update `max_length` to be the maximum of `max_length` and the length of the current window (excluding one zero).
            max_length = max(max_length, r - l)

            # Move the `r` pointer forward.
            r += 1

        return max_length