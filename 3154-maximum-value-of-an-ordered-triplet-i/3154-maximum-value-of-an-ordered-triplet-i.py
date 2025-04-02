class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_triplet = 0
        left = nums[0]

        for j in range(1,n):
            if nums[j] > left:
                left = nums[j]
            for k in range(j + 1,n):
                max_triplet = max(max_triplet,(left - nums[j]) * nums[k])
        
        return max_triplet
                