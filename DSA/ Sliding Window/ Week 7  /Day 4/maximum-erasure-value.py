class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        r , l = 0 , 0 
        curr_sum , max_sum = 0 , 0

        # iterate over the input nums list 
        while r < len(nums):
            # adding the elemnts to the set unique to get unique sums that are max
            if nums[r] not in unique:
                unique.add(nums[r])
                curr_sum += nums[r]
                r += 1
                max_sum = max(max_sum,curr_sum)
            else:
                unique.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
        return max_sum 

        