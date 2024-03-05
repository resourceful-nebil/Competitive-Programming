class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        ans.add(tuple([]))
        subset = []
        
        def backtrack(i,subset):
            if len(subset) == len(nums):
                return 
           
            
            x = 0
            for i in range(i,len(nums)):
                # if nums[i] not in subset:
                subset.append(nums[i])
                temp = tuple(subset[:])
                ans.add(temp)
                backtrack(i + 1,subset)
                x= subset.pop()

                

        backtrack(0, [])
        return list(ans)