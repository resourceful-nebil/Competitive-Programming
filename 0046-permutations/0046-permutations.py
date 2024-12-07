class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        if len(nums) == 1:
            return [nums]
        
        def dfs(i):
            if len(path) == len(nums):
                res.append(path[:])
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(i + 1)
                    path.pop()
        
        dfs(0)
        return res