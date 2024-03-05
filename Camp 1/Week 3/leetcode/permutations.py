class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        if len(nums) == 1:
            return [nums[:]]

        def backtrack(i,path):
            if len(path) == len(nums):
                ans.append(path[:])
                return 
            
            
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(i + 1,path)
                    path.pop()
        
        backtrack(0,path)
        return ans