class Solution:
    def canCross(self, stones: List[int]) -> bool:
        _stones = {st:i for i,st in enumerate(stones)}
        # print(_stones)
        if stones[1]-stones[0]>1:
            return False

        @lru_cache(maxsize=None)
        def dfs(i, jump):
            if i == len(stones) - 1:
                return True
            
            for next_jump in range(jump - 1, jump + 2):
                if next_jump > 0:
                    next_position = stones[i] + next_jump
                    if next_position in _stones:
                        if dfs(_stones[next_position], next_jump):
                            return True
            return False
        
        return dfs(0, 0)