class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        max_index = 0

        for i in range(n):
            if max_index < i:
                return False
            if nums[i] + i < max_index:
                continue
            else:
                max_index = nums[i] + i
        return True
        
        # i = 0
        # while i < n:
        #     if  nums[i] == 0 and n == 1:
        #         return True 
        #     if nums[i] == 0 and nums[i] == nums[-1]:
        #         return True 
        #     if nums[i] == 0:
        #         return False
        #     i += nums[i] 
            
        
        # return True 