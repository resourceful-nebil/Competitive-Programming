class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        taregt = total // 2

        memo = {}
        def dp(i,target):
            if (i,target) in memo:
                return memo[(i,target)]

            if i == len(nums):
                if target == 0:
                    return True
                else:
                    return False
            if target < 0:
                return False
            if target == 0:
                return True
        
            val = dp(i + 1,target - nums[i]) or dp(i+1,target)

            memo[(i,target)] = val
            return val
        
        return dp(0,taregt)

            

            
