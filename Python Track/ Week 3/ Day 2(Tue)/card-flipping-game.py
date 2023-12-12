
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        # used to store values found in both lists
        not_good = set()
        # used to store the min good number
        minimum_good = 10**9

        # to store values found in both lists by iterating on both
        for front,back in zip(fronts,backs):
            if front == back:
                not_good.add(front)
        
        # to check if values that are in not_good set aren't found in fronts list
        for val in fronts:
            if val not in not_good:
                minimum_good = min(minimum_good,val)

        # to check if values that are in not_good set aren't found in backs list
        for val in backs:
            if val not in not_good:
                minimum_good = min(minimum_good,val)

        return 0 if minimum_good == 10**9 else minimum_good            
