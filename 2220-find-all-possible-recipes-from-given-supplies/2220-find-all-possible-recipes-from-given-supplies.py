class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for recipe, req_indgi in zip(recipes,ingredients):
            for indgi in req_indgi:
                graph[indgi].append(recipe)
            indeg[recipe] += len(req_indgi)
        
        q = deque(supplies)
        ans = []

        while q:
            for _ in range(len(q)):
                indgi = q.popleft()
                for r in graph[indgi]:
                    indeg[r] -= 1
                    if indeg[r] == 0:
                        ans.append(r)
                        q.append(r)
        return ans