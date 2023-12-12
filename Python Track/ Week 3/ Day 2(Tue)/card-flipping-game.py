
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        not_good = set()
        minimum_good = 10**9

        for front,back in zip(fronts,backs):
            if front == back:
                not_good.add(front)
        
        for val in fronts:
            if val not in not_good:
                minimum_good = min(minimum_good,val)
        
        for val in backs:
            if val not in not_good:
                minimum_good = min(minimum_good,val)

        return 0 if minimum_good == 10**9 else minimum_good            
