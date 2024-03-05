class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        ans = set()
        path = []
        if sum(candidates) < n:
            return []


        def backtrack(i,path):
            if sum(path) == n and len(path) == k:
                temp = tuple(path[:])
                ans.add(temp)
                return 
            if sum(path) > n:
                return 
            x = 0
            for i in range(i,len(candidates)):
                if candidates[i] != x:

                    path.append(candidates[i])
        
                    backtrack(i + 1,path)
                    x = path.pop()

        
        backtrack(0,path)
        
        return list(ans)