class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        window_sum = 0

        # Using for loop because in every iteration right pointer will increase by one 
        for right in range(len(nums)):
            window_sum += nums[right]

            # checking if the window sum is greater or not 
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0

