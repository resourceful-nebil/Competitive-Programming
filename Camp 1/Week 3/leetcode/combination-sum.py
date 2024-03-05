class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(i,path):
            if sum(path) == target:
                ans.append(path[:])
                return 
            if sum(path) > target:
                return 
            
            for i in range(i,len(candidates)):
                path.append(candidates[i])
                backtrack(i,path)
                path.pop()
                    


        
        backtrack(0,path)
        return ans
                
            



