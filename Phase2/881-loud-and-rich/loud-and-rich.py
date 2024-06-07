class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [-1] * n
        graph = defaultdict(list)
        for rich, poor in richer:
            graph[poor].append(rich)
      
        def dfs(i):
            if ans[i] != -1:
                return

            ans[i] = i
            for nei in graph[i]:
                dfs(nei)
                if quiet[ans[nei]] < quiet[ans[i]]:
                    ans[i] = ans[nei]

        for i in range(n):
            dfs(i)

        return ans