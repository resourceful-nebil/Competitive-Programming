class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0] * n
        for u,v in edges:
            indeg[v] += 1
        # print(indeg)
        cnt = 0
        for i,n in enumerate(indeg):
            if n == 0:
                cnt += 1
    
        return -1 if cnt > 1 else indeg.index(0)