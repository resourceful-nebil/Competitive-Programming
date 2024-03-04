class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        subset = []
        
        def backtrack(i,subset):
            if len(subset) == len(nums):
                return 
            if i >= len(nums):
                return 
            
            subset.append(nums[i])
            ans.append(subset[:])
            backtrack(i + 1,subset)
            subset.pop()

            backtrack(i + 1, subset)

        backtrack(0, [])
        return ans
            
            
