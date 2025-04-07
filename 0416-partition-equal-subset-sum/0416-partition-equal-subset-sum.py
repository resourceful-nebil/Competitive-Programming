class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False 
        
        n = len(nums)
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(n - 1, -1, -1):
            nextDp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        
        return True if target in dp else False