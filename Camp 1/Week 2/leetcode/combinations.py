class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(fn,path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for num in range(fn, n + 1):
                path.append(num)
                backtrack(num + 1,path)
                path.pop()
        
        backtrack(1,path)
        return ans 