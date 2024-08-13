class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        path = []
        candidates.sort()
        if sum(candidates) < target:
            return []


        def backtrack(i,path):
            if sum(path) == target:
                temp = tuple(path[:])
                ans.add(temp)
                return 
            if sum(path) > target:
                return 
            x = 0
            for i in range(i,len(candidates)):
                if candidates[i] != x:

                    path.append(candidates[i])
        
                    backtrack(i + 1,path)
                    x = path.pop()
                    


        
        backtrack(0,path)
        # res = []
        # for r in ans:
        #     r.sort()
        #     if r not in res:
        #         res.append(r)
        

        # print(res)
        return list(ans)