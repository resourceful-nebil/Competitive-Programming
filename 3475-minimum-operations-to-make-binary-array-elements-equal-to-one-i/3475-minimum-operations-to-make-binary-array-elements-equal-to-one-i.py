class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zeros = 0
        cnt = 0

        for i in range(n - 2):
            if nums[i] == 0:
                cnt += 1
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
            
        return -1 if 0 in nums else cnt
            